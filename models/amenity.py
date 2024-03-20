#!/usr/bin/python3
"""
Module containing the Amenity class, a subclass of BaseModel.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity offered by a place to stay.

    Attributes:
        name (str): Name of the amenity.
        id (str): Unique identifier for the amenity (inherited from BaseModel).
        created_at (datetime): Time when the amenity was created (inherited
        from BaseModel).
        updated_at (datetime): Time when the amenity was last updated
        (inherited from BaseModel).
    """

    name = ""  # Default value for the name attribute

    def __init__(self, *args, **kwargs):
        """
        Initializes a new Amenity instance.

        Args:
            *args: Positional arguments passed to the BaseModel constructor.
            **kwargs: Keyword arguments passed to the BaseModel constructor,
            including the 'name' attribute.
        """
        super().__init__(self, *args, **kwargs)