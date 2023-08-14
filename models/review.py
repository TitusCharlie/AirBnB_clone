#!/usr/bin/python3
"""import modules"""

from models.base_model import BaseModel


"""
=====================================================
Represent a review.
Attributes:

    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
=====================================================
"""


class Review(BaseModel):
    
    place_id = "" #string - empty string: it will be the Place.id
    user_id = "" #string - empty string: it will be the User.id
    text = "" #string - empty string
