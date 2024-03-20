#!/usr/bin/python3

"""
This module contains the foundational BaseModel class for the AirBnB clone
project.
It provides essential attributes and methods for managing object state.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Defines the base model for all other classes in this AirBnB clone project.

    Attributes:
        id (str): Unique identifier generated using UUID version 4.
        created_at (datetime): Timestamp of object creation.
        updated_at (datetime): Timestamp of the last object modification.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.

        Args:
            *args: Unused.
            **kwargs (dict): Key-value pairs of attributes.

        If kwargs is provided:
            * Attributes from kwargs are set on the object.
            * 'created_at' and 'updated_at' strings are converted
            to datetime objects.
        If kwargs is not provided:
            * Generates a unique UUID (id).
            * Sets the current datetime for 'created_at' and 'updated_at'.
            * Calls storage.new() to register the object
            (likely for persistence).
        """

        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a user-friendly string representation of the
        BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime
        and persists the object's state by calling storage.save().
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Creates a dictionary representation of the BaseModel instance.

        Returns:
            dict: Contains key-value pairs of the instance's attributes,
                  with datetime objects converted to ISO format strings.
                  Includes the '__class__' key for object type identification.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict