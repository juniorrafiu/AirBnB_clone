
from uuid import uuid4
from datetime import datetime
import models 

class BaseModel():
    """
    Defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel
        """
        if kwargs:
            for key, value in kwargs.items():
                
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                    setattr(self, key, value)
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return str of information of BaseModel.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ 
        Updates the public instance attribute
        updated_at
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        dict = {"__class__": self.__class__.__name__, "created_at": self.created_at.isoformat(
        ), "updated_at": self.updated_at.isoformat()}
        dict_copy = self.__dict__.copy()
        dict_copy.update(dict)
        return dict_copy