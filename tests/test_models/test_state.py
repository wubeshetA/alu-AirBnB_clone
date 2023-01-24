#!/usr/bin/python3
"""unittest for User class"""
import unittest
from models.state import State


class TestBaseModel(unittest.TestCase):
    """Test cases for User class."""

    def setUp(self):
        self.testState = State()

    def test_name(self):
        self.assertIsInstance(self.testState.name, str)


if __name__ == "__main__":
    unittest.main()
