#!/usr/bin/env python
"""A module that that serializes instances to a JSON file and deserializes
JSON file to instances"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:

    # private class attributes
    # __file_path is the path to the JSON file to store all objects.
    __file_path = 'storage.json'

    # __objects is a dictionary that stores all objects by <class name>.id
    # ex: to store a BaseModel object with id=12121212, the key will be
    # BaseModel.12121212 and the value will be the object.
    # the object (value of key) is stored like this:
    # <models.base_model.BaseModel object at 0x7f3329dac310>
    __objects = {}

    def all(self):
        return self.__objects

    # sets in __objects the obj with key <obj class name>.id
    def new(self, obj):
        """Add obj with key <obj class name>.id to dictionary.

        Args:

        obj: the object with key <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        # json_data = json.dump(obj)
        self.__objects[key] = obj

    # serializes __objects to the JSON file (path: __file_path)
    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path)."""
        json_obj = {}
        for key in self.__objects.keys():
            json_obj[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as json_file:
            json.dump(json_obj, json_file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file"""
        """(path: __file_path) exists ; otherwise, do nothing."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as json_file:
                json_obj = json.load(json_file)
                for key in json_obj.keys():

                    # By providing the dict value stored in json_obj[key] as
                    # kwargs, genrate an object with the same attributes
                    self.__objects[key] = eval(
                        json_obj[key]['__class__'])(**json_obj[key])
