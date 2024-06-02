import unittest
import os
from models.base_model import BaseModel
from models.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_storage.json"
        self.storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        # Add some data to storage
        self.storage.new(self.base_model)
        self.storage.save()

        # Check if data is retrieved correctly
        all_data = self.storage.all()
        self.assertTrue(isinstance(all_data, dict))
        self.assertIn(self.base_model.__class__.__name__ +
                      "." + self.base_model.id, all_data)

    def test_new_and_save(self):
        # Create a new BaseModel instance
        new_model = BaseModel()
        new_model.name = "Test Model"
        new_model.save()

        # Check if the model is saved correctly in storage
        self.assertIn(new_model.__class__.__name__ + "." +
                      new_model.id, self.storage._FileStorage__objects)

    def test_reload(self):
        # Save some data to storage
        self.storage.new(self.base_model)
        self.storage.save()

        # Create a new storage instance and reload data
        new_storage = FileStorage()
        new_storage.reload()

        # Check if data is reloaded correctly
        all_data = new_storage.all()
        self.assertTrue(isinstance(all_data, dict))
        self.assertIn(self.base_model.__class__.__name__ +
                      "." + self.base_model.id, all_data)


if __name__ == "__main__":
    unittest.main()
