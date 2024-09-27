from typing import List, Optional, Type

from pydantic import BaseModel
from sqlalchemy import delete, insert, update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.base import Base
from utilities.exceptions import ObjectNotFound


class CRUDBase:
    """
    A generic CRUD class for managing any SQLAlchemy model.

    Attributes:
        model (Type[Base]): The SQLAlchemy model to be used for the CRUD
        operations.
    """

    def __init__(self, model: Type[Base]) -> None:
        """
        Initialize the CRUDBase with a specific model.

        Args:
            model (Type[Base]): The SQLAlchemy model for CRUD operations.
        """
        self.model = model

    async def read_by_id(
        self, db: AsyncSession, obj_id: int
    ) -> Optional[Base]:
        """
        Retrieve an object by its ID from the database.

        Args:
            db (AsyncSession): The asynchronous database session.
            obj_id (int): The ID of the object to retrieve.

        Returns:
            Optional[Base]: The retrieved object, or None if no object is
            found.
        """
        statement = select(self.model).where(self.model.id == obj_id)
        result = await db.execute(statement)
        obj = result.scalars().first()
        return obj if obj else None

    async def read_multi(
        self, db: AsyncSession, limit: int = 100, offset: int = 0
    ) -> List[Optional[Base]]:
        """
        Retrieve all objects from the database.

        Args:
            limit: Limit of ojcets in response
            offset: Offset in response
            db (AsyncSession): The asynchronous database session.

        Returns:
            Optional[List[Base]]: A list of all objects, or an empty list
            if no objects are found.
        """
        statement = select(self.model).limit(limit).offset(offset)
        result = await db.execute(statement)
        objects = result.scalars().all()
        return objects if objects else []

    async def create(
        self,
        db: AsyncSession,
        create_data: Type[BaseModel],
    ) -> Base:
        """
        Create a new object in the database.

        Args:
            db (AsyncSession): The asynchronous database session.
            create_data (Base): The data needed to create the object.

        Raises:
            SQLAlchemyError: If any error occurs during the database operation.

        Returns:
            Base: The newly created object.
        """
        try:
            data = create_data.model_dump()
            statement = insert(self.model).values(**data).returning(self.model)
            result = await db.execute(statement)
            await db.commit()
            return result.scalars().first()

        except SQLAlchemyError as err:
            await db.rollback()
            raise RuntimeError(
                "Failed to create object in the database."
            ) from err

    async def update(
        self,
        db: AsyncSession,
        update_data: Type[BaseModel],
        obj_id: int,
    ) -> Optional[Base]:
        """
        Update an existing object in the database.

        Args:
            db (AsyncSession): The asynchronous database session.
            update_data (Base): The data to update the object with.
            obj_id (int): The ID of the object to update.

        Raises:
            SQLAlchemyError: If any error occurs during the database operation.

        Returns:
            Optional[Base]: The updated object
        """
        try:
            data = update_data.model_dump(exclude_unset=True)
            statement = (
                update(self.model)
                .where(self.model.id == obj_id)
                .values(**data)
                .returning(self.model)
            )
            result = await db.execute(statement)
            await db.commit()
            return result.scalars().first()

        except SQLAlchemyError as err:
            await db.rollback()
            raise RuntimeError(
                "Failed to update object in the database."
            ) from err

    async def remove(
        self,
        db: AsyncSession,
        obj_id: int,
    ) -> None:
        """
        Remove an object from the database by its ID.

        Args:
            db (AsyncSession): The asynchronous database session.
            obj_id (int): The ID of the object to be removed.

        Raises:
            ObjectNotFound: If the object with the given ID is not found.
            SQLAlchemyError: If any error occurs during the database operation.


        Returns:
            None
        """
        try:
            if (obj := await db.get(self.model, obj_id)) is None:  # noqa F841
                raise ObjectNotFound(
                    object_name=self.model.__name__, object_id=obj_id
                )

            statement = delete(self.model).where(self.model.id == obj_id)
            await db.execute(statement)
            await db.commit()

        except SQLAlchemyError as err:
            await db.rollback()
            raise RuntimeError(
                "Failed to remove object from the database."
            ) from err
