#!/usr/bin/python3
"""FileStorage tests"""

from models.base_model import BaseModel
import models
import os
import unittest

class TestEngine(unittest.TestCase):
    """Tests for the engine storage"""

    def setUp(self):
        """Sets Up the enviroment for tests"""
        if os.path.exists('file.json'):
            os.remove("file.json")