# import unittest
# from models.engine.file_storage import FileStorage
# from models import storage
# from models.base_model import BaseModel


# class TestFileStorage(unittest.TestCase):
#     """Tests for FileStorage class"""

#     def setUp(self):
#         """Set up for tests"""
#         self.testModel = BaseModel()

#     # def test_file_path(self):
#     #     """Test if file path is a string"""
#     #     self.assertIsInstance(self.storage.__file_path, str)

#     # def test_all(self):
#     #     """Test if all method returns a dictionary"""
#     #     self.assertIsInstance(storage.all(), dict)

#     def test_new(self):
#         """Test if new method adds a new object to __objects"""
#         objects_before_new = storage.all() # returns a dict from storage

#         print("==============Before=======================")
#         print(objects_before_new.keys())
#         # print("==============After=======================")
#         storage.new(self.testModel) # adds a new object to __objects
#         storage.save()

#         objects_after_new = storage.all()
#         print("==============After=======================")
#         print(objects_after_new.keys())
#         self.assertNotEqual(len(objects_before_new), len(objects_after_new))

#     def tearDown(self):
#         """Tear down for tests"""
#         del self.testModel


# if __name__ == "__main__":
#     unittest.main()
