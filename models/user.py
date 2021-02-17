#!/usr/bin/python3
"""[summary]
"""
import models


class User(models.base_model.BaseModel):
    """[summary]

    Args:
        models ([type]): [description]
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
