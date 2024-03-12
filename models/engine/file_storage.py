#!/usr/bin/python3

"""
This file defines the storage system for
the project.
It will use JSON format to either serialize and deserialize objects
"""

import json


class FileStorage:
    """
        This is  will serve as an Object relation mappingto interface or database
    """

    """class private varaibles"""
    __file_path: str = "file.json"
    __objects: dict = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        json_dict = {}
        for key, obj in self.__objects.items():
            json_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                json_dict = json.load(file)
                for key, value in json_dict.items():
                    class_name, obj_id = key.split('.')
                    class_ = eval(class_name)
                    self.__objects[key] = class_(**value)
        except FileNotFoundError:
            pass