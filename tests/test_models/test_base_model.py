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

    
if __name__ == "__main__":
    unittest.main()
