#!/usr/bin/env python
"""A module that that serializes instances to a JSON file and deserializes JSON file to instances"""

import json
import os

class FileStorage:
    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        return self.__objects

    # sets in __objects the obj with key <obj class name>.id
    def new(self, obj):
        """Add obj with key <obj class name>.id to dictionary.
        
        Args: 
        
        obj: the object with key <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = str(obj)

    # serializes __objects to the JSON file (path: __file_path)
    def save(self):

        with open(self.__file_path, 'w') as json_file:
            json.dump(self.__objects, json_file)

    def reload(self):
        """ Loads objects from JSON file."""

        try:
            with open(self.__file_path) as json_file:
                self.__objects = json.load(json_file)
        except FileNotFoundError as exception:
            return