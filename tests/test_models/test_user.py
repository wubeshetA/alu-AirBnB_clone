#!/usr/bin/python3
"""unittest for User class"""
import unittest
from models import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User class."""

    def setUp(self):
        self.testUser = User()

    def test_user(self):
        """Test if User class is subclass of BaseModel."""
        self.assertTrue(issubclass(self.testUser.__class__, BaseModel))

    def test_email(self):
        """Test email class attribute."""
        self.assertIsInstance(self.testUser.email, str)

    def test_password(self):
        self.assertIsInstance(self.testUser.password, str)

    def test_first_name(self):
        self.assertIsInstance(self.testUser.first_name, str)

    def test_last_name(self):
        self.assertIsInstance(self.testUser.last_name, str)


if __name__ == '__main__':
    unittest.main()
