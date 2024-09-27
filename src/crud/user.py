from crud.base import CRUDBase
from models.user import User


class CRUDUser(CRUDBase):
    """
    A specific CRUD class for managing User objects.

    This class inherits from CRUDBase and provides an interface for performing
    CRUD operations specifically on User instances in the database.

    Inherits:
        CRUDBase: A generic CRUD class for managing SQLAlchemy models.
    """

    ...


crud_user = CRUDUser(User)
"""
An instance of CRUDUser for managing User objects.

This instance can be used to perform create, read, update, and delete
operations on User instances in the database.
"""
