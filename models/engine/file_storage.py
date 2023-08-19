#!/usr/bin/python3
"""
===============
import modules
===============
"""

import json
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


class FileStorage:
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        # FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
        key = f"{type(obj).__name__}.{id(obj)}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        stored_objects = FileStorage.__objects
        stored_objects_dictionary = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as file:
                json.dump(stored_objects_dictionary, file)

    def reload(self):
        """deserializes the JSON file to __objects 
           (only if the JSON file (__file_path) exists ; 
           otherwise, do nothing. If the file doesn’t exist,
           no exception should be raised)"""
        try:
             with open(FileStorage.__file_path) as file:
                  json.load(file)

        except:
             pass
        