#!/usr/bin/python3
import unittest
from datetime import datetime
import uuid
from models.base_model import BaseModel

class TestBaseModelInit(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_init(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)
        self.assertEqual(self.base_model.created_at, self.base_model.updated_at)


class TestBaseModelSave(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_save(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertEqual(old_updated_at, new_updated_at)


class TestBaseModelToDict(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_to_dict(self):
        self.base_model.my_number = 123
        self.base_model.name = "Test Model"
        obj_dict = self.base_model.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["my_number"], 123)
        self.assertEqual(obj_dict["name"], "Test Model")
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["updated_at"], self.base_model.updated_at.isoformat())
        self.assertEqual(obj_dict["id"], self.base_model.id)
        self.assertEqual(obj_dict["created_at"], self.base_model.created_at.isoformat())


class TestBaseModelStr(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_str(self):
        expected_string = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_string)


class TestBaseModelInitFromDict(unittest.TestCase):
    def test_init_from_dict(self):
        model_dict = {
            "id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
            "created_at": "2017-09-28T21:03:54.052298",
            "__class__": "BaseModel",
            "my_number": 89,
            "updated_at": "2017-09-28T21:03:54.052302",
            "name": "My_First_Model"
        }
        my_model = BaseModel(**model_dict)

        self.assertEqual(my_model.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")
        self.assertEqual(my_model.my_number, 89)
        self.assertEqual(my_model.name, "My_First_Model")
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertEqual(my_model.created_at, datetime.strptime("2017-09-28T21:03:54.052298", '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertEqual(my_model.updated_at, datetime.strptime("2017-09-28T21:03:54.052302", '%Y-%m-%dT%H:%M:%S.%f'))

if __name__ == '__main__':
    unittest.main()