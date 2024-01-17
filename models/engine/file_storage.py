#!/usr/bin/python3

"""
Defines the FileStorage class: serializes instances to a JSON file
and deserializes JSON file to instances:
"""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file
    and deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key
        <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects
        to the JSON file (path: __file_path)"""
        temp_dict = {}
        for key, value in self.__objects.items():
            temp_dict[key] = value.to_dict
        with open(self.__file_path, 'w') as f:
            json.dump(temp_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path) as f:
                loaded_objects = json.load(f)
            for key, obj_data in loaded_objects.items():
                class_name = key.split('.')[0]
                self.new(eval(class_name)(**obj_data))

        except FileNotFoundError:
            pass
