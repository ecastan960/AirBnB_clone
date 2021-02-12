#!/usr/bin/python3
"""unitary test for Base Class"""

from models import BaseModel
import unittest
import pep8

Base = BaseModel.BaseModel

class BaseTests(unittest.TestCase):
    """Tests for Base class"""

        def test_module_docs(self):
        """Test for module docstring"""
        pass

    def test_class_docs(self):
        """Test for Base docstring"""
        pass

    def test_pep8_main_file(self):
        """Test pep8 ok."""
        pass

    def test_pep8_test(self):
        """Test pep8 ok."""
        pass

    def test_correct_id(self):
        """Checks if Base is handling _nb_objects OK"""
        pass


if __name__ == "__main__":
    unittest.main()