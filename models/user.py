#!/usr/bin/python3
"""import modules"""

from base_model import BaseModel


"""
=====================================================
Represent a User.
Attributes:
    email (str): The email of the user.
    password (str): The password of the user.
    first_name (str): The first name of the user.
    last_name (str): The last name of the user.
=====================================================
"""


class User(BaseModel):
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
