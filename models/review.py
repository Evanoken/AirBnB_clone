#!/usr/bin/python3
"""
Contains Review Class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ review class has public attributes """
    place_id = ""
    user_id = ""
    text = ""
