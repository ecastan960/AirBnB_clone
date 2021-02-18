#!/usr/bin/python3
"""User tests"""

import unittest
from models.amenity import Amenity


class TestUser(unittest.TestCase):
    """Checks if user is working"""

    def test_simpleinstantiation(self):
        """Checks if a user is created ok"""

        self.assertEqual(type(Amenity.name), str)
        self.assertEqual(Amenity.name, "")
