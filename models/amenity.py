#!/usr/bin/python3
# File: amenity.py
# Main Authors: Dominic Gitau
# email(s): <dominicnjoroge1@gmail.com>
#           
""" Amenity Module for HBNB project """
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """Represents an amenity data set."""
    __tablename__ = 'amenities'
    name = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
