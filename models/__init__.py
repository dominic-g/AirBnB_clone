#!/usr/bin/python3
# File: __init__.py
# Main Authors: Dominic Gitau
# email(s): <dominicnjoroge1@gmail.com>
#           

"""This module is A unique FileStorage/DBStorage instance for all models"""
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

storage = DBStorage() if os.getenv(
    'AIRBNB_TYPE_STORAGE') == 'db' else FileStorage()

storage.reload()
