#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class is the driving force or the back bone
    for this project. All the methods that is used to
    fetch the data from a file and send the data to a file is
    existed in this function. Uderstanding this class is the
    crucial part of the project
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return the dictionary representation of the
        instances"""
        if not cls:
            return self.__objects
        return {k: v for k, v in self.__objects.items() if type(v) == cls}

    def delete(self, obj=None):
        """ To delete a specific instance """
        if obj:
            className = obj.__class__.__name__ + '.' + obj.id
            if className in self.__objects.keys():
                del self.__objects[className]

    def new(self, obj):
        """To set in instances in the __objects dictionary"""
        className = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[className] = obj

    def save(self):
        """To save instances in the json file"""
        json_obj = {
                key: v.to_dict() for key, v in FileStorage.__objects.items()
                }
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(json_obj, json_file, indent=2)

    def reload(self):
        """To fetch data from a json file"""
        try:
            with open(FileStorage.__file_path) as json_file:
                objects = json.load(json_file)
            for value in objects.values():
                className = value["__class__"]
                self.new(eval(className + "(**value)"))
        except Exception:
            pass
