#!/usr/bin/python3
"""The driving power of relational databses"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import create_engine, MetaData

__classNames = [
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"]

class DBStorage():
    """ This class comprises the ORM methods that helps us
    to interact with our detabase """

    __classNames = [
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"]

    __engine = None
    __session = None

    def __init__(self):
        """ This is how we get conneted to the database.
        The four environmental variables are used for
        robust security """

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)
    """
    def all(self, cls=None):
        #query to fetch all objects related to cls if cls
        #is not None. Otherwise fetch all

        list_obj = []
        if not cls:
           # [list_obj.append(obj) for obj 
           #in session.query(__classNames)]
           for obj in DBStorage.__classNames:
               list_obj += self.__session.query(obj)
        else:
            list_obj = self.__session.query(cls)

        #return the dictionary reperesentation
        #return {v.__class__.__name__ + '.' + v.id: v for v in list_obj
        return {type(v).__name__ + '.' + v.id: v for v in list_obj}
    """
    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)


    def new(self, obj):
        """ Adding the obj to the database """
        self.__session.add(obj)

    def save(self):
        """ commiting all changes to a database """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete a session object if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ To Create all the tables on the database """
        from sqlalchemy.orm import sessionmaker
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(
                bind=self.__engine, expire_on_commit=False
                )
        self.__session = Session()

    def close(self):
        """ calls remove()
        """
        self.__session.close()
