import unittest
import sys
import time

sys.path.append('/home/wubeshet/alu/alu-AirBnB_clone')

from models.base_model import BaseModel
class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def setUp(self):
        self.myModel = BaseModel()

    def test_save(self):
        # test it before and after save()
        updated_at_before_save = self.myModel.updated_at
        time.sleep(0.5)
        self.myModel.save()
        updated_at_after_save = self.myModel.updated_at
        self.assertNotEqual(updated_at_before_save, updated_at_after_save)

if __name__ == "__main__":
    unittest.main()