#!/user/bin/python3
"""place module for the AirBnB clone"""

from models import BaseModel


class Place(BaseModel):
    """Place class"""

    # class attributes
    city_id = ""  # string - empty string: it will be the City.id
    user_id = ""  # string - empty string: it will be the User.id
    name = ""  # string - empty string
    description = ""  # string - empty string
    number_rooms = 0  # integer - 0
    number_bathrooms = 0  # integer - 0
    max_guest = 0  # integer - 0
    price_by_night = 0  # integer - 0
    latitude = 0.0  # float - 0.0
    longitude = 0.0  # float - 0.0
    amenity_ids = []  # list of string - empty list: it will be the list of
    # Amenity.id later

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
