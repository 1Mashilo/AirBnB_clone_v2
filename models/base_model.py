from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime
import models

Base = declarative_base()

class BaseModel:
    """
    Defines the base model for all other classes in this AirBnB clone project.

    Attributes:
        id (str): Unique identifier generated using UUID version 4.
        created_at (datetime): Timestamp of object creation.
        updated_at (datetime): Timestamp of the last object modification.
    """

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.

        Args:
            *args: Unused.
            **kwargs (dict): Key-value pairs of attributes.

        If kwargs is provided:
            * Attributes from kwargs are set on the object.
            * 'created_at' and 'updated_at' strings are converted to datetime objects.
        If kwargs is not provided:
            * Generates a unique UUID (id).
            * Sets the current datetime for 'created_at' and 'updated_at'.
            * Calls save() to register the object (likely for persistence).
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.save()

    def __str__(self):
        """
        Returns a user-friendly string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime
        and persists the object's state by calling models.storage.save().
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
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
        obj_dict.pop('_sa_instance_state', None)
        return obj_dict

    def delete(self):
        """
        Deletes the current instance from storage.
        """
        models.storage.delete(self)
