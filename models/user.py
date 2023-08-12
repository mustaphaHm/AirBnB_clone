#!/usr/bin/python3
"""User model."""
from models.base_model import BaseModel


class User(BaseModel):
    """Definition of class User."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
