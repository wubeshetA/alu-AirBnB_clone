#!/usr/bin/python3
import unittest
import time
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def setUp(self):
        self.testModel = BaseModel()

    # test BaseModel before and after clling save method
    def test_save(self):
        updated_at_before_save = self.testModel.updated_at
        time.sleep(0.5)
        self.testModel.save()
        updated_at_after_save = self.testModel.updated_at
        self.assertNotEqual(updated_at_before_save, updated_at_after_save)

    # test BaseModel to_dict method return type
    def test_to_dict_return(self):
        testModel_dict = self.testModel.to_dict()
        self.assertIsInstance(testModel_dict, dict)
    
    # test BaseModel to_dict method for it's content.
    def test_to_dict_value(self):
        testModel_dict = self.testModel.to_dict()
        self.assertIn('__class__', testModel_dict)
    
    # test BaseModel to_dict method if it's content has the correct types
    def test_to_dict_content_type(self):
        testModel_dict = self.testModel.to_dict()
        self.assertIsInstance(testModel_dict.get('created_at'), str)
        self.assertIsInstance(testModel_dict.get('created_at'), str)
    
    # test string value of BaseModel
    def test__str__(self):
        class_name = self.testModel.__class__.__name__
        id = self.testModel.id
        dict_v = self.testModel.__dict__
        self.assertEqual(str(self.testModel), f"[{class_name}] ({id}) {dict_v}")
        
if __name__ == "__main__":
    unittest.main()
