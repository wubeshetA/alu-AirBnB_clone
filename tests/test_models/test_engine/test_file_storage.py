import os
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage class"""

    def setUp(self):
        """Set up for tests"""
        self.testModel = BaseModel()

    def tearDown(self):
        """Tear down for tests"""
        del self.testModel

    def test_file_path(self):
        """Test if file path is a string and private variable"""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_objects(self):
        """Test if objects is a dictionary and private variable"""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_all(self):
        """Test if all method returns a dictionary"""
        self.assertEqual(type(storage.all()), dict)

    def test_new(self):
        """Test if new method populates the __object attribute"""
        storage.new(self.testModel)
        self.assertNotEqual(FileStorage._FileStorage__objects, {})
        objects_key = (self.testModel.__class__.__name__ + '.' +
                       self.testModel.id)
        # check if __objects as
        self.assertIn(objects_key, FileStorage._FileStorage__objects.keys())

    def test_save(self):
        """Test if save method saves the __objects attribute to a file"""
        storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload(self):
        """Test if reload method reloads the __objects attribute from a file"""
        storage.reload()
        self.assertNotEqual(FileStorage._FileStorage__objects, {})

    # def test_reload_empty(self):
    #     """Test if reload method does nothing if file is empty"""
    #     os.remove(FileStorage._FileStorage__file_path)
    #     storage.reload()
    #     print("__file_path -> ", FileStorage._FileStorage__file_path)
    #     print(FileStorage._FileStorage__objects)
    #     self.assertEqual(FileStorage._FileStorage__objects, {})


if __name__ == "__main__":
    unittest.main()
