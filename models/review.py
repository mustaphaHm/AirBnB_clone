#!/usr/bin/python3
"""User Review."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Definition of class Review."""

    place_id = ""
    user_id = ""
    text = ""
