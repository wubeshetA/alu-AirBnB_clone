#!/usr/bin/python3
"""unittest for User class"""
import unittest
from models.state import State
from models import BaseModel


class TestState(unittest.TestCase):
    """Test cases for User class."""

    def setUp(self):
        self.testState = State()

    def testState(self):
        self.assertTrue(issubclass(self.testState.__class__, BaseModel))

    def test_name(self):
        self.assertIsInstance(self.testState.name, str)


if __name__ == "__main__":
    unittest.main()
