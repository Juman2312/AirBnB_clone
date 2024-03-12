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

    def __init__(self, file_path="C:\Users\Dedo-PC\Desktop\AirBnB_clone\models\engine\file_storage.py"):
        self.file_path = file_path
        self.__objects = {}

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
        try:
            with open(self.file_path, 'w') as file:
                json.dump(json_dict, file)
        except IOError:
            print(f"Error: Unable to write to file {self.file_path}")

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.file_path, 'r') as file:
                json_dict = json.load(file)
                for key, value in json_dict.items():
                    class_name, obj_id = key.split('.')
                    class_ = eval(class_name)
                    self.__objects[key] = class_(**value)
        except FileNotFoundError:
            print(f"Error: File {self.file_path} not found")
        except (json.JSONDecodeError, ValueError):
            print(f"Error: Invalid JSON in file {self.file_path}")
