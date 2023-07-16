#!/usr/bin/python3
'''This module creates a AirBnB Review class'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Class for managing AirBnB review objects'''
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        '''Initializes attributes for the AirBnB review class'''
        super().__init__(*args, **kwargs)
