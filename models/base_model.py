#!/usr/bin/python3
"""This module contains the BaseModel class"""

from datetime import datetime
import uuid

class BaseModel:
    """Base class for all common attributes and methods"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def __str__(self):
        """Return a string representation of BaseModel"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """Update the updated_at attribute"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Return a dict representation of the BaseModel"""
        self.__dict__['created_at'] = datetime.isoformat(self.created_at )
        self.__dict__['updated_at'] = datetime.isoformat(self.updated_at)
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__


        
