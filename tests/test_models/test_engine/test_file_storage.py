#!/usr/bin/python3
"""FileStorage tests"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import models
import os
import unittest


class TestEngine(unittest.TestCase):
    """Tests for the engine storage"""

    def setUp(self):
        """Sets Up the enviroment for tests"""
        if os.path.exists('file.json'):
            os.remove("file.json")

    def test_simple_instantiation(self):
        """Test if a simple instance is sucessful created"""

        new_storage = FileStorage()
        self.assertEqual(type(new_storage), FileStorage)

    def test_all_method(self):
        """Test for all method"""

        self.assertEqual(type(models.storage.all()), dict)

    def test_new_method(self):
        """Test for the new method of FileStorage"""

        my_model = BaseModel()
        len1 = len(models.storage.all())
        my_model.id = 56
        models.storage.new(my_model)
        len2 = len(models.storage.all())
        self.assertTrue(len1 < len2)


if __name__ == '__main__':
    unittest.main()
