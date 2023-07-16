#!/usr/bin/python3
'''This module creates a AirBnB User class'''
from models.base_model import BaseModel


class User(BaseModel):
    '''Class for managing AirBnB user objects'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        '''Initializes attributes for the AirBnB User class'''
        super().__init__(*args, **kwargs)
