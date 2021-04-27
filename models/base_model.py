#!/usr/bin/python3
"""This file defines a basemodel class
"""

import models
import uuid
import datetime

str_to_date = datetime.datetime.strptime


class BaseModel:
    """defines all common attributes/methods
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """Initiation function
        """
        if kwargs:
            for key in kwargs:
                if key != "__class__":
                    setattr(self, key, kwargs[key])
            self.created_at = str_to_date(kwargs['created_at'],
                                          '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = str_to_date(kwargs['updated_at'],
                                          '%Y-%m-%dT%H:%M:%S.%f')

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Convert object into string
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """ updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return (my_dict)
