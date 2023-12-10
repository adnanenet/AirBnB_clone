#!/usr/bin/python3
"""Defines the BaseModel class."""

import uuid
from datetime import datetime


class BaseModel:
    """This reperesents the BaseModel class of the HBnB Project."""
    def __init__(self):
    """" Initialises a new BaseModel instance.
    Args:
        *args(any): unused.
        *kwargs (dict): key/value pairs of attributes.
    """
    self.id = str(uuid.uuid4())
    self.created_at = datetime.today()
    self.updated_at = datetime.today()
