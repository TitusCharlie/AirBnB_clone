#!/usr/bin/python3
"""import modules"""

from models.base_model import BaseModel


"""
=====================================================
Represent a City.
Attributes:
    
state_id: string - empty string: it will be the State.id
name: string - empty string
=====================================================
"""


class City(BaseModel):

    name = ""
    state_id = ""