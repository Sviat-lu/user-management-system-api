from typing import Dict, Optional

from email_validator import EmailNotValidError
from fastapi.exceptions import RequestValidationError
from pydantic import (
    BaseModel,
    EmailStr,
    field_validator,
    model_validator,
    validate_email,
)


class UserBase(BaseModel):
    """
    Base model for user-related data. This model contains the common attributes
    that are shared between different user operations such as creating,
    updating, and retrieving users.

    Attributes:
        - name (str): User's name.
        - email (EmailStr): User's email.
        - phone (str): User's phone number.
        - note (str): Note about user.
    """

    name: str
    email: EmailStr
    phone: str
    note: str

    @field_validator("email")
    def validate_email(email: str):
        try:
            # returns ("display_name", "full email")
            email_info: tuple = validate_email(email)
            validated_email = email_info[1]
        except EmailNotValidError as err:
            raise err
        return validated_email


class UserResponse(UserBase):
    """
    Response model for a user. This model inherits from UserBase and is used
    to return user data from the API, such as when retrieving a user or
    listing users.

    Inherits:
        UserBase: The base user attributes (name, email, phone, note).
    """

    id: int


class UserCreate(UserBase):
    """
    Model for creating a new user. This model is used when a client sends
    data to the API to create a new user in the system.

    Inherits:
        UserBase: The base user attributes (name, email, phone, note) that
        are required for creating a user.
    """

    ...


class UserUpdate(UserBase):
    """
    Model for updating an existing user. This model allows partial updates to
    the user's fields, meaning both `date_to_do` and `user_info` are optional.
    If provided, they will overwrite the existing data.

    Attributes:
        - date_to_do (Optional[datetime]): The updated date and time for the
        user (optional).
        user_info (Optional[str]): The updated user information (optional).

    Inherits:
        UserBase: The base user attributes, though they are optional for
        updates.

    Raises:
        RequestValidationError: If neither `date_to_do` nor `user_info` is
        provided for the update.
    """

    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    note: Optional[str] = None

    @model_validator(mode="before")
    def check_fields(update_data: Dict):
        """
        Validates that at least one field is provided when updating a user.
        If neither field is provided, it raises a validation error.

        Raises:
            RequestValidationError: If no field is specified.

        Example:
            If a user tries to update a user without specifying any fields to
            change, this validation will trigger to ensure that at least one
            field is being updated.
        """
        if not update_data:
            raise RequestValidationError(
                "Please specify at least one field to change."
            )
        return update_data
