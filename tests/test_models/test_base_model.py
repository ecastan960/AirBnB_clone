#!/usr/bin/python3

from models.base_model import BaseModel
import unittest


class Test_basics(unittest.TestCase):
    """ Simple tests """

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
        """ Tests that default attr are set even with args """

        my_model = BaseModel("test", 18)
        
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

if __name__ == "__main__":
    unittest.main()
