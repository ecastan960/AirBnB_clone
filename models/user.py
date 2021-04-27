#!/usr/bin/python3
"""
Class user that inherits from BaseModel
"""
import models


class User(models.base_model.BaseModel):
    """User class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
