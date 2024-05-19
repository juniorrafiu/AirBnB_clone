#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel():
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        dict = {"__class__": self.__class__.__name__, "created_at": self.created_at.isoformat(
        ), "updated_at": self.updated_at.isoformat()}
        return dict
