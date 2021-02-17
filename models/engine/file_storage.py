#!/usr/bin/python3
"""Filestorage class"""

import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State


class FileStorage:
    """G"""

    __file_path = "file.json"
    __objects = {}

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
            previous_objects = {}
            with open(self.__file_path, 'r', encoding='utf8') as f:
                previous_objects = json.load(f)
            for key in previous_objects:
                lookUpClass = key.split('.')
                if lookUpClass[0] == "BaseModel":
                    self.__objects[key] = BaseModel(**previous_objects[key])
                elif lookUpClass[0] == "User":
                    self.__objects[key] = User(**previous_objects[key])
                elif lookUpClass[0] == "Place":
                    self.__objects[key] = Place(**previous_objects[key])
                elif lookUpClass[0] == "State":
                    self.__objects[key] = State(**previous_objects[key])
                elif lookUpClass[0] == "City":
                    self.__objects[key] = City(**previous_objects[key])
                elif lookUpClass[0] == "Amenity":
                    self.__objects[key] = Amenity(**previous_objects[key])
                elif lookUpClass[0] == "Review":
                    self.__objects[key] = Review(**previous_objects[key])
