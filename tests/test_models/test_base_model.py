#!/usr/bin/python3

"""
    Defines a class TestBaseModel.
"""
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """Represent a TestBaseModel."""

    def test_id_is_uuid(self):
        """Test that id is a valid UUID"""
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
        try:
            uuid_obj = uuid.UUID(base_model.id, version=4)
        except ValueError:
            self.fail("id is not a valid UUID")
        self.assertEqual(str(uuid_obj), base_model.id)

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime object"""
        base_model = BaseModel()
        self.assertIsInstance(base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object"""
        base_model = BaseModel()
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_str_method(self):
        """Test the __str__ method"""
        base_model = BaseModel()
        expected_str = f"[BaseModel] ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(str(base_model), expected_str)

    def test_save_method(self):
        """Test the save method updates updated_at"""
        base_model = BaseModel()
        old_updated_at = base_model.updated_at
        base_model.save()
        new_updated_at = base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertTrue(new_updated_at > old_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(
            base_model_dict['created_at'], base_model.created_at.isoformat())
        self.assertEqual(
            base_model_dict['updated_at'], base_model.updated_at.isoformat())
        self.assertEqual(base_model_dict['id'], base_model.id)


if __name__ == '__main__':
    unittest.main()
