#!/usr/bin/python3
"""unittest for User class"""
import unittest
from models.review import Review
from models import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for User class."""

    def setUp(self):
        self.testReview = Review()

    def testState(self):
        self.assertTrue(issubclass(self.testReview.__class__, BaseModel))

    def test_place_id(self):
        self.assertIsInstance(self.testReview.place_id, str)

    def test_user_id(self):
        self.assertIsInstance(self.testReview.user_id, str)

    def test_text(self):
        self.assertIsInstance(self.testReview.text, str)


if __name__ == "__main__":
    unittest.main()
