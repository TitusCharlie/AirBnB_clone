#!/usr/bin/python3
"""
    module imports for base models
"""

from uuid import uuid4
from datetime import datetime
"""
===============================
Base model for the AriBnB clone
===============================
"""


class BaseModel:
    """create objects for the class"""
    today = datetime.now()


    def __init__(self):
        self.created_at = self.today
        self.updated_at = self.today
        self.id = str(uuid4())
        # self.__class__ = self.__class__.__name__
    
    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = self.today

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy["created_at"] = self.created_at.isoformat()
        return dict_copy



    def __str__(self):
        """Return the str representation of the model"""

        return f"{(self.__class__.__name__)} {(self.id)} {self.__dict__}"
    