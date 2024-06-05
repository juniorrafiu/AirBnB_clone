import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage():
    __file_path = 'file.json'  # this is the path that we will store the serialised info
    __objects = {}  # an empty dictionary to store the object instances by <class name>.id

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            json.dump({key: value.to_dict()
                      for key, value in self.__objects.items()}, f, indent=4)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                from_json = json.load(f)
                for key, value in from_json.items():
                    class_name = value.pop('__class__')
                    self.new(eval(class_name)(**value))

        except FileNotFoundError:
            pass
