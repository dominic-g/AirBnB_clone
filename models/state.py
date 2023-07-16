#!/usr/bin/python3
'''This module creates a AirBnB State class'''
from models.base_model import BaseModel


class State(BaseModel):
    '''Class for managing AirBnB state objects'''
    name = ""

    def __init__(self, *args, **kwargs):
        '''Initializes attributes for the AirBnB State class'''
        super().__init__(*args, **kwargs)
