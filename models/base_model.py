#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Definition of class BaseModel"""
    def __init__(self, *args, **kwargs):
        """Default Constructor"""
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs is not None:
            kwargs.pop("__class__", None)
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, date_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Overiding the str Method to print a specific format"""
        cls_name = __class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
    """Public Methods"""

    def save(self):
        """updates the public instance updated_at
        with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
