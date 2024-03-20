#!/usr/bin/python3

"""
This module defines the User class, representing a user within the application.
The User class inherits from the BaseModel class.

Attributes:
    email (str): The user's email address.
    password (str): The user's password.
    first_name (str): The user's first name.
    last_name (str): The user's last name.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize User class"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""