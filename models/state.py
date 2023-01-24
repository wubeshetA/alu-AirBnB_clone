#!/user/bin/python3
"""state module for the AirBnB clone"""

from models import BaseModel


class State(BaseModel):
    """State class"""

    # class attributes
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
