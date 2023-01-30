#!/usr/bin/python3
"""user module for the AirBnB clone"""

from models import BaseModel


class Review(BaseModel):
    """Review class"""

    place_id = ""  # string - empty string: it will be the Place.id
    user_id = ""  # string - empty string: it will be the User.id
    text = ""  # string - empty string

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
