#!/usr/bin/python3
"""This module contains the BaseModel class"""

from datetime import datetime
import models
import uuid


class BaseModel:
    """Base class for all common attributes and methods"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel"""

        # if keyword argument is provided initialize class with the specified
        # values
        if kwargs != {}:
            for key, val in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at':
                    val = datetime.fromisoformat(val)
                elif key == 'updated_at':
                    val = datetime.fromisoformat(val)
                self.__setattr__(key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

            #
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of BaseModel"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return a dict representation of the BaseModel"""

        formated_dict = self.__dict__.copy()
        formated_dict['created_at'] = formated_dict['created_at'].isoformat()
        formated_dict['updated_at'] = formated_dict['updated_at'].isoformat()
        formated_dict['__class__'] = self.__class__.__name__
        return formated_dict
