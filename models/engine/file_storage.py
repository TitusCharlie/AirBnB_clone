#!/usr/bin/python3
"""
===============
import modules
===============
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


"""
==============================================
class that serializes instances to a JSON file 
and deserializes JSON file to instances
==============================================
"""


class FileStorage():
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        # FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """deserializes the JSON file to __objects 
           (only if the JSON file (__file_path) exists ; 
           otherwise, do nothing. If the file doesn’t exist,
           no exception should be raised)"""
        try:
            if os.path.exists(self.__file_path):
                with open(self.__file_path, 'r') as f:
                    self.__objects = json.load(f)
                    for k, v in self.__objects.items():
                        self.__objects[k] = BaseModel(**v)

        except:
             return
        