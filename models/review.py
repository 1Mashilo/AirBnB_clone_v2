#!/usr/bin/python3


"""
This module defines the Review class, representing a user-submitted
review associated with a rental property.
The Review class inherits from the BaseModel class

Attributes:
    place_id (str): ID of the Place the review is for.
    user_id (str): ID of the user who wrote the review.
    text (str): The content of the review.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize Review class"""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""