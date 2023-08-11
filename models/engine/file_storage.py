#!user/bin/python3
import json

from models.base_model import BaseModel


class FileStorage:
    """DEfinition of class FileStorage"""
    __file_path = "file.json"
    __objects = {}
    """public instance methods"""
    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf_8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        try:
            path = FileStorage.__file_path
            with open(path, mode="r", encoding="utf_8") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value['__class__']
                    cls = BaseModel
                    if class_name == 'BaseModel':
                        obj = cls(**value)
                        FileStorage.__objects[key] = obj
                    else:
                        pass
        except FileNotFoundError:
            pass