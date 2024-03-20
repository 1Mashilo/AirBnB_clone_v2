#!/usr/bin/python3

"""
This module defines the City class, representing a geographical city.
The City class inherits from the BaseModel class.

Attributes:
    state_id (str): ID of the state the city is located in.
    name (str): Name of the city.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize City class"""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""