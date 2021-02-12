#!/usr/bin/python3
"""[summary]

Returns:
    [type]: [description]
"""

import uuid
import datetime


class BaseModel:

    def __init__(self):
        """[summary]
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """[summary]
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        self.updated_at = datetime.datetime.now()
        my_dict["__class__"] = self.__class__.__name__
        return (my_dict)
