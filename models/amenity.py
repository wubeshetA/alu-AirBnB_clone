#!/usr/bin/python3
"""Amenity module for the AirBnB clone"""

from models import BaseModel


class Amenity(BaseModel):
    """Amenity class"""

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
