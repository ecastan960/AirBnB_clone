#!/usr/bin/python3
"""This file creates a class
that inherits from BaseModel
"""
import models


class Review(models.base_model.BaseModel):
    """Review class
    """
    place_id = ""
    user_id = ""
    text = ""
