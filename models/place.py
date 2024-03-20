#!/usr/bin/python3

"""
This module defines the Place class, which represents a rental
property or accommodation.
The Place class inherits from the BaseModel class (likely providing
core data-management functionality).

Attributes:
    city_id (str): ID of the city the place is located in.
    user_id (str): ID of the owner of the place.
    name (str): Name of the place.
    description (str): Description of the place.
    number_rooms (int): Number of rooms in the place.
    number_bathrooms (int): Number of bathrooms.
    max_guest (int): Maximum number of guests allowed.
    price_by_night (int): Price per night.
    latitude (float): Latitude coordinate.
    longitude (float): Longitude coordinate.
    amenity_ids (list): List of amenity IDs associated with the place.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Place class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize Place class"""
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []