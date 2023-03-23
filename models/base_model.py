#!/usr/bin/python3
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, Table, ForeignKey
"""This is class is the parent class of the rest
of the classes in this project, namely, User, State,
Amenity, Place, and Review. This class comprises the
comman methods and attributes that is used in other
classes.
"""
Base = declarative_base()



class BaseModel:
    """Defining the init method to initialize the
    the attributes"""

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        if kwargs:
            directives = "%Y-%m-%dT%H:%M:%S.%f"
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, directives)
                else:
                    self.__dict__[key] = val

        if 'id' not in kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    
    def __str__(self):
        """To return the standard string to print function"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def save(self):
        """Save either crated or updated instances"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Puting the data in the dict object"""
        _dict = self.__dict__.copy()
        _dict["__class__"] = self.__class__.__name__
        _dict["created_at"] = self.created_at.isoformat()
        _dict["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in self.__dict__:
            del _dict['_sa_instance_state']
        return _dict

    def delete(self):
        """ This method deletes an instance """
        models.storage.delete(self)
