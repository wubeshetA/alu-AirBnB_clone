#!/usr/bin/python3
"""unittest for User class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for User class."""

    def setUp(self):
        self.testCity = City()

    def test_state_id(self):
        self.assertIsInstance(self.testCity.state_id, str)

    def test_name(self):
        self.assertIsInstance(self.testCity.name, str)


if __name__ == "__main__":
    unittest.main()
