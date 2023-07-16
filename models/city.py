#!/usr/bin/python3
'''This module creates a AirBnB User class'''
from models.base_model import BaseModel


class City(BaseModel):
    '''Class for managing AirBnB city objects'''
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        '''Initializes attributes for the AirBnB city class'''
        super().__init__(*args, **kwargs)
