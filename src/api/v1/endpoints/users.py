from typing import List, Optional

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from crud import crud_user
from databases import get_async_session
from models.user import User
from schemas import UserCreate, UserResponse, UserUpdate
from utilities.exceptions import UserNotFound

router = APIRouter()


@router.get(
    path="/",
    response_model=List[UserResponse],
    status_code=status.HTTP_200_OK,
    summary="Retrieve all users",
    description=("Fetches a list of all users stored in the database."),
)
async def read_users_multi(
    limit: int = 100,
    offset: int = 0,
    db: AsyncSession = Depends(get_async_session),
):
    """
    Fetch all users.

    This endpoint returns all users from the database.

    Args:
        limit: Limit of users in response
        offset: Offset in response
        db (AsyncSession): The asynchronous session for database access.

    Returns:
        List[UserResponse]: A list of all users if found or empty list
        if not found.
    """
    return await crud_user.read_multi(db=db, limit=limit, offset=offset)


@router.get(
    path="/{user_id}/",
    status_code=status.HTTP_200_OK,
    response_model=UserResponse,
    summary="Retrieve a user by ID",
    description=(
        "Returns information about a specific user by its unique ID. "
        "If the user is not found, an error is returned."
    ),
)
async def read_user(
    user_id: int,
    db: AsyncSession = Depends(get_async_session),
):
    """
    Fetch a user by ID.

    This endpoint returns the details of a specific user by its ID. If the user
    does not exist, an error will be raised.

    Args:
        user_id (int): The unique identifier of the user.
        db (AsyncSession): The asynchronous session for database access.

    Returns:
        UserResponse: The user data if found.

    Raises:
        UserNotFound: If the user with the given ID does not exist.
    """
    user: User = await crud_user.read_by_id(db=db, obj_id=user_id)
    if not user:
        raise UserNotFound(user_id)
    return user


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse,
    summary="Create a new user",
    description=("Creates a new user in the database."),
)
async def create_user(
    create_data: UserCreate,
    db: AsyncSession = Depends(get_async_session),
):
    """
    Create a new user.

    This endpoint creates a new user in the database.

    Args:
        create_data (UserCreate): The data required to create a new user.
        db (AsyncSession): The asynchronous session for database access.

    Returns:
        UserResponse: The created user data.
    """
    return await crud_user.create(db=db, create_data=create_data)


@router.patch(
    "/{user_id}/",
    status_code=status.HTTP_200_OK,
    response_model=Optional[UserResponse],
    summary="Update a user by ID",
    description=(
        "Updates an existing user by its unique ID. "
        "If the user is not found, 404 error is returned."
    ),
)
async def update_user(
    user_id: int,
    update_data: UserUpdate,
    db: AsyncSession = Depends(get_async_session),
):
    """
    Update a user by ID.

    This endpoint updates the details of an existing user by its ID.
    If the user does not exist, an error will be raised.

    Args:
        user_id (int): The unique identifier of the user to be updated.
        update_data (UserUpdate): The data to update the user with.
        db (AsyncSession): The asynchronous session for database access.

    Returns:
        Optional[UserResponse]: The updated user data if the update was
        successful.

    Raises:
        UserNotFound: If the user with the given ID does not exist.
    """
    updated_user: User = await crud_user.update(
        db=db,
        update_data=update_data,
        obj_id=user_id,
    )
    if not updated_user:
        raise UserNotFound(user_id)
    return updated_user


@router.delete(
    "/{user_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a user by ID",
    description=(
        "Deletes an existing user by its unique ID. "
        "If the user is not found, 404 error is returned."
    ),
)
async def remove_user(
    user_id: int,
    db: AsyncSession = Depends(get_async_session),
):
    """
    Delete a user by ID.

    This endpoint deletes an existing user from the database by its ID.
    If the user does not exist, 404 error will be raised.

    Args:
        user_id (int): The unique identifier of the user to be deleted.
        db (AsyncSession): The asynchronous session for database access.

    Raises:
        UserNotFound: If the user with the given ID does not exist.
    """
    await crud_user.remove(db=db, obj_id=user_id)
