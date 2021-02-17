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
        """Testing if args are ignored"""

        my_model = BaseModel("test", 18)

        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

    def test_kwargs(self):
        """Unpacked dictionary as argument"""

        my_dict = {'id': '99h15869-ki5k-5r9p-f0y1-t168f8b27636',
             'created_at': '2020-02-16T11:03:58.053312',
             'updated_at': '2020-02-16T11:06:59.053312'}

        my_model = BaseModel(**my_dict)

        self.assertEqual(my_model.id, '99h15869-ki5k-5r9p-f0y1-t168f8b27636')
        self.assertEqual(my_model.created_at.isoformat(),
                         '2020-02-16T11:03:58.053312')
        self.assertEqual(my_model.updated_at.isoformat(),
                         '2020-02-16T11:06:59.053312')

        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertTrue(hasattr(my_model, "__class__"))
        self.assertTrue(my_model.__class__ not in my_model.__dict__)

    def test_kwargs_with_class(self):
        """Unpacked dictionary has 'class' key and is ignored"""

        my_dict = {'id': '99h15869-ki5k-5r9p-f0y1-t168f8b27636',
             'created_at': '2020-02-16T11:03:58.053312',
             'updated_at': '2020-02-16T11:06:59.053312',
             '__class__': 'BaseModel'}

        my_model = BaseModel(**my_dict)

        self.assertEqual(my_model.id, '99h15869-ki5k-5r9p-f0y1-t168f8b27636')
        self.assertEqual(my_model.created_at.isoformat(),
                         '2020-02-16T11:03:58.053312')
        self.assertEqual(my_model.updated_at.isoformat(),
                         '2020-02-16T11:06:59.053312')

        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertTrue(hasattr(my_model, "__class__"))
        self.assertTrue(my_model.__class__ not in my_model.__dict__)
        

if __name__ == "__main__":
    unittest.main()
