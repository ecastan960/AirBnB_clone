#!/usr/bin/python3
"""This file creates a class
that inherits from BaseModel
"""
import models


class City(models.base_model.BaseModel):
    """City class
    """
    state_id = ""
    name = ""
