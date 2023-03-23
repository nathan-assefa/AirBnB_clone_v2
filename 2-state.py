#!/usr/bin/python3
""" This script defines the class State that
inherit from the Base class in order to have
the built in functionalites of the sqlachemy """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    """ Defining a state class """

    __tablename__ = 'states'

    if environ['HBNB_TYPE_STORAGE'] == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
                'City', cascade='all, delete', backref='state'
                )

    else:
        @property
        def cities(self):
            """ This getter function gets all the city having
            retation with a State instance via the primary and
            foreign key relationship.
            Since this is one to many relatinship,
            only one state can be mapped to multiple cities.
            This is done by compairing City.state_id == self.id
            self in this case demonistrate the current instance of
            the State class
            """

            from models import storage
            #first we need to fetch all the city from the database
            all_city = storage.all(City)
            fitered_city = []

            for city in all_city.values():
                if city.state_id == self.id:
                    filtered_city.append(city)

            return filterd_city

