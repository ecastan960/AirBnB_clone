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
