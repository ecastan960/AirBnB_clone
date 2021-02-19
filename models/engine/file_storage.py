#!/usr/bin/python3
"""Filestorage class
"""

import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State
import inspect
import sys


class FileStorage:
    """[summary]

    Returns:
        [type]: [description]
    """

    __file_path = "file.json"
    __objects = {}

    y = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    clases = [command[0] for command in y]

    def all(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__objects

    def new(self, obj):
        """[summary]

        Args:
            obj ([type]): [description]
        """
        self.__objects[str(obj.__class__.__name__) + "." + str(obj.id)] = obj

    def save(self):
        """[summary]
        """
        serializable_dict = {}
        for element in self.__objects:
            serializable_dict[element] = self.__objects[element].to_dict()

        with open(self.__file_path, 'w', encoding='utf8') as f:
            json.dump(serializable_dict, f)

    def reload(self):
        """[summary]
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf8') as f:
                previous_objects = json.load(f)
            for key in previous_objects:
                lookUpClass = key.split('.')
                if lookUpClass[0] in self.clases:
                    self.__objects[key] = eval(str(lookUpClass[0]) + "(**previous_objects[key])")
