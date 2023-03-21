#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    """Represent a city.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'))
    if environ['HBNB_TYPE_STORAGE'] == 'db':
        cities = relationship(
                'City', cascade='all, delete', backref='state'
                )
    else:
        @property
        def cities(self):
            """Getter method for cities
            Return: list of cities with state_id equal to self.id
            """
            from models import storage
            from models.city import City
            # return list of City objs in __objects
            cities_dict = storage.all(City)
            cities_list = []

            # copy values from dict to list
            for city in cities_dict.values():
                if city.state_id == self.id:
                    cities_list.append(city)

            return cities_list
