from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    """
    Represents the 'user' table in the database, used to store user-related
    information.

    Attributes:
        - id (int): The primary key of the user.
        - name (str): User's name.
        - email (str): User's email.
        - phone (str): User's phone number.
        - note (str): Note about user.
    """

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=255))
    email: Mapped[str] = mapped_column(String(length=255))
    phone: Mapped[str] = mapped_column(String(length=255))
    note: Mapped[str] = mapped_column(String(length=255))
