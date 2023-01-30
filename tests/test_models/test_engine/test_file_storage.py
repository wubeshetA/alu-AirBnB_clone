import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage class"""

    def setUp(self):
        """Set up for tests"""
        self.testModel = BaseModel()

    def test_file_path(self):
        """Test if file path is a string and private variable"""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def tearDown(self):
        """Tear down for tests"""
        del self.testModel


if __name__ == "__main__":
    unittest.main()
