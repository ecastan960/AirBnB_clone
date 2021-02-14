#!/usr/bin/python3
"""Filestorage class"""

import json
from os import path
import models

class FileStorage:
    """G"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[str(obj.__class__.__name__) + "." + str(obj.id)] = obj

    def save(self):
        serializable_dict = {}
        for element in self.__objects:
            serializable_dict[element] = self.__objects[element].to_dict()

        with open(self.__file_path, 'w', encoding='utf8') as f:
            json.dump(serializable_dict, f)

    def reload(self):
        if path.exists(self.__file_path):
            previous_objects = {}
            with open(self.__file_path, 'r') as f:
                previous_objects = json.load(f)
            for element in previous_objects:
                self.__objects[element] = models.BaseModel(previous_objects[element])

