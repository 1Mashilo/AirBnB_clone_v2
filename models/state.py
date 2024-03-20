#!/usr/bin/python3

"""
This module defines the State class, representing a geographical
state or province.
The State class inherits from the BaseModel class.

Attributes:
    name (str): Name of the state.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize State class"""
        super().__init__(*args, **kwargs)
        self.name = ""