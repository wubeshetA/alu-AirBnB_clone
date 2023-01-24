#!/usr/bin/python3
from models import BaseModel

class User(BaseModel):
    """User class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
