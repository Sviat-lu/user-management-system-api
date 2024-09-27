from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    The base class for all models in the database.
    It uses SQLAlchemy's DeclarativeBase to define a common foundation
    for all tables.
    """

    ...
