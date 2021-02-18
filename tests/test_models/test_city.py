#!/usr/bin/python3
"""User tests"""

import unittest
from models.city import City


class TestUser(unittest.TestCase):
    """Checks if user is working"""

    def test_simpleinstantiation(self):
        """Checks if a user is created ok"""

        self.assertEqual(type(City.name), str)
        self.assertEqual(type(City.state_id), str)
        self.assertEqual(City.name, "")
        self.assertEqual(City.state_id, "")
