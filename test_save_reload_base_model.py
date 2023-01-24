#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all() # returns the dictionary __objects
                        # ex: {'BaseModel.12121212': <BaseModel object>}
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_1_Model"
my_model.my_number = 89
my_model.bool = True
my_model.save() # calls save() method of FileStorage
                # it damps to json file in the following way:

                # {"BaseModel.4d0b5eca-f942-4a0d-bbae-c30ac4c81318": {"id": "4d0b5eca-f942-4a0d-bbae-c30ac4c81318", "created_at": "2023-01-23T07:45:02.420123", "updated_at": "2023-01-23T07:45:02.420139", "name": "My_sec_Model", "my_number": 89, "bool": true, "__class__": "BaseModel"}}
print(my_model)  # prints the string representation of my_model as follows:
                # [BaseModel] (4d0b5eca-f942-4a0d-bbae-c30ac4c81318) {'id': '4d0b5eca-f942-4a0d-bbae-c30ac4c81318', 'created_at': datetime.datetime(2023, 1, 23, 7, 45, 2, 420123), 'updated_at': datetime.datetime(2023, 1, 23, 7, 45, 2, 420139), 'name': 'My_sec_Model', 'my_number': 89, 'bool': True}

print("--------------------------------")
# print(my_model.id)