#!/usr/bin/python3
"""[summary]

Returns:
    [type]: [description]
"""

import uuid
import datetime
import storage
str_to_date = datetime.datetime.strptime


class BaseModel:

    def __init__(self, *args, **kwargs):
        """[summary]
        """
        if kwargs:
            self.id = kwargs["id"]
            self.created_at = str_to_date(kwargs["created_at"],
                                          '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = str_to_date(kwargs["updated_at"],
                                          '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new()

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
        storage.save()

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
