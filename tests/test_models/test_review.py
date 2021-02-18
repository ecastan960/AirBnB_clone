#!/usr/bin/python3
"""User tests"""

import unittest
from models.review import Review


class TestUser(unittest.TestCase):
    """Checks if user is working"""

    def test_simpleinstantiation(self):
        """Checks if a user is created ok"""

        self.assertEqual(type(Review.place_id), str)
        self.assertEqual(type(Review.user_id), str)
        self.assertEqual(type(Review.text), str)
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")
