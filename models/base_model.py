#!/usr/bin/python3
import models
from uuid import uuid4
from datetime import datetime
"""This is class is the parent class of the rest
of the classes in this project, namely, User, State,
Amenity, Place, and Review. This class comprises the
comman methods and attributes that is used in other
classes.
"""


class BaseModel:
    """Defining the init method to initialize the
    the attributes"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            directives = "%Y-%m-%dT%H:%M:%S.%f"
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, directives)
                else:
                    self.__dict__[key] = val

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """To return the standard string to print function"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def save(self):
        """Save either crated or updated instances"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Puting the data in the dict object"""
        _dict = self.__dict__.copy()
        _dict["__class__"] = self.__class__.__name__
        _dict["created_at"] = self.created_at.isoformat()
        _dict["updated_at"] = self.updated_at.isoformat()
        return _dict
