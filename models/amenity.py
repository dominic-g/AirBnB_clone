#!/usr/bin/python3
'''This module creates a AirBnB Amenity class'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Class for managing AirBnB amenity objects'''
    name = ""

    def __init__(self, *args, **kwargs):
        '''Initializes attributes for the AirBnB Amenity class'''
        super().__init__(*args, **kwargs)
