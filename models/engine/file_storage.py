#!/usr/bin/python3
"""Filestorage class"""

import json

class FileStorage:
    """G"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[str(obj.__class__.__name__) + "." + str(self.id)] = obj

    def save(self):
        with open(self.__file_path, 'w', encoding='utf8') as f:
            json.dump(self.__objects, f)

    def reload(self):
        with open(self.__file_path, 'r', encoding='utf8') as f:
            data = json.load(f)
        return data

