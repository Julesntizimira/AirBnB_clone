#!/usr/bin/python3
"""
module contains place information and properties
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    place class with attributes
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, **kwargs):
        """constructor method"""
        super().__init__(**kwargs)
