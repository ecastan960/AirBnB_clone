#!/usr/bin/python3
"""User tests"""

import unittest
from models.state import State


class TestUser(unittest.TestCase):
    """Checks if user is working"""

    def test_simpleinstantiation(self):
        """Checks if a user is created ok"""

        self.assertEqual(type(State.name), str)
        self.assertEqual(State.name, "")
