import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        """Reset storage before each test"""
        storage.all().clear()

    def test_create(self):
        """Test the create command"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            self.assertIn("BaseModel", storage.all())
            new_id = output.getvalue().strip()
            self.assertIn(f"BaseModel.{new_id}", storage.all())

    def test_show(self):
        """Test the show command"""
        new_instance = BaseModel()
        new_instance.save()
        new_id = new_instance.id

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(f"show BaseModel {new_id}")
            self.assertIn(f"{new_instance}", output.getvalue().strip())

    def test_destroy(self):
        """Test the destroy command"""
        new_instance = BaseModel()
        new_instance.save()
        new_id = new_instance.id

        with patch('sys.stdout', new=StringIO()):
            HBNBCommand().onecmd(f"destroy BaseModel {new_id}")
            self.assertNotIn(f"BaseModel.{new_id}", storage.all())

    def test_all(self):
        """Test the all command"""
        new_instance1 = BaseModel()
        new_instance2 = User()
        new_instance1.save()
        new_instance2.save()

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all")
            self.assertIn(f"{new_instance1}", output.getvalue().strip())
            self.assertIn(f"{new_instance2}", output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all BaseModel")
            self.assertIn(f"{new_instance1}", output.getvalue().strip())
            self.assertNotIn(f"{new_instance2}", output.getvalue().strip())

    def test_update(self):
        """Test the update command"""
        new_instance = BaseModel()
        new_instance.save()
        new_id = new_instance.id

        with patch('sys.stdout', new=StringIO()):
            HBNBCommand().onecmd(f'update BaseModel {new_id} name "test_name"')
            self.assertEqual(storage.all()[f"BaseModel.{new_id}"].name, "test_name")

    def test_update_missing_value(self):
        """Test the update command when value is missing"""
        new_instance = BaseModel()
        new_instance.save()
        new_id = new_instance.id

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(f'update BaseModel {new_id} name')
            self.assertIn("** value missing **", output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
