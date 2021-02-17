#!/usr/bin/python3
"""[summary]
"""
import models


class Review(models.base_model.BaseModel):
    """[summary]

    Args:
        models ([type]): [description]
    """
    place_id = ""
    user_id = ""
    text = ""
