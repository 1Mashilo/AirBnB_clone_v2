#!/usr/bin/python3

"""
This module defines the City class, representing a geographical city.
The City class inherits from the BaseModel class.

Attributes:
    state_id (str): ID of the state the city is located in.
    name (str): Name of the city.
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """
    Represents a City for the AirBnB clone project.

    Attributes:
        __tablename__ (str): Name of the table in the database.
        name (str): Name of the city.
        state_id (str): ID of the state the city is located in.
    """

    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")