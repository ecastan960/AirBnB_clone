#!/usr/bin/python3
"""User tests"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Checks if user is working"""

    def test_simpleinstantiation(self):
        """Checks if a user is created ok"""

        my_user = User()
        self.assertEqual(type(User.email), str)
        self.assertEqual(type(User.password), str)
        self.assertEqual(type(User.first_name), str)
        self.assertEqual(type(User.last_name), str)
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")
