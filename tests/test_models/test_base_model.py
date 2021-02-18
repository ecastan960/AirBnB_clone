#!/usr/bin/python3

from models.base_model import BaseModel
from datetime import datetime
import unittest
import json
import os
import models


my_dict = {'id': '99h15869-ki5k-5r9p-f0y1-t168f8b27636',
           'created_at': '2020-02-16T11:03:58.053312',
           'updated_at': '2020-02-16T11:03:58.053312'}


class TestBasics(unittest.TestCase):
    """ Simple tests """
    def setUp(self):
        """Sets Up the enviroment for tests"""
        if os.path.exists('file.json'):
            os.remove("file.json")

    def test_simple_creation(self):
        """ No arguments """
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

    def test_multiple_id(self):
        """Each id must be diferent"""
        model1 = BaseModel()
        model2 = BaseModel()
        model3 = BaseModel()

        self.assertFalse(model1.id == model2.id)
        self.assertFalse(model1.id == model3.id)
        self.assertFalse(model2.id == model3.id)

    def test_ignore_args(self):
        """Testing if args are ignored"""

        my_model = BaseModel("test", 18)

        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

    def test_kwargs(self):
        """Unpacked dictionary as argument"""

        my_model = BaseModel(**my_dict)

        self.assertEqual(my_model.id, '99h15869-ki5k-5r9p-f0y1-t168f8b27636')
        self.assertEqual(my_model.created_at.isoformat(),
                         '2020-02-16T11:03:58.053312')
        self.assertEqual(my_model.updated_at.isoformat(),
                         '2020-02-16T11:03:58.053312')

        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertTrue(hasattr(my_model, "__class__"))
        self.assertTrue(my_model.__class__ not in my_model.__dict__)

    def test_kwargs_and_args(self):
        """Unpacked dictionary as argument and args ignored"""

        my_model = BaseModel(18, "test", **my_dict)

        self.assertEqual(my_model.id, '99h15869-ki5k-5r9p-f0y1-t168f8b27636')
        self.assertEqual(my_model.created_at.isoformat(),
                         '2020-02-16T11:03:58.053312')
        self.assertEqual(my_model.updated_at.isoformat(),
                         '2020-02-16T11:03:58.053312')

        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertTrue(hasattr(my_model, "__class__"))
        self.assertTrue(my_model.__class__ not in my_model.__dict__)

    def test_kwargs_with_class(self):
        """Unpacked dictionary has 'class' key and is ignored"""

        my_model = BaseModel(**my_dict)

        self.assertEqual(my_model.id, '99h15869-ki5k-5r9p-f0y1-t168f8b27636')
        self.assertEqual(my_model.created_at.isoformat(),
                         '2020-02-16T11:03:58.053312')
        self.assertEqual(my_model.updated_at.isoformat(),
                         '2020-02-16T11:03:58.053312')

        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertTrue(hasattr(my_model, "__class__"))
        self.assertTrue(my_model.__class__ not in my_model.__dict__)

    def test_dete_converted_datatype(self):
        """Conversion from string to datetype is executed"""

        my_model = BaseModel(**my_dict)

        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.updated_at), datetime)

    def test_save_method(self):
        """Checks if JSON file is created"""

        my_model = BaseModel()
        my_model.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_str_method(self):
        """Checks for str in base_model"""

        my_model = BaseModel()

        name = "[{}] ({}) {}".format(my_model.__class__.__name__,
                                     my_model.id,
                                     my_model.__dict__)
        self.assertEqual(name, my_model.__str__())

    def test_to_dict(self):
        """Checks the to_dict method of BaseModel"""

        my_model = BaseModel(**my_dict)
        new_dict = my_dict.copy()
        new_dict['__class__'] = "BaseModel"
        self.assertEqual(new_dict, my_model.to_dict())


if __name__ == "__main__":
    unittest.main()
