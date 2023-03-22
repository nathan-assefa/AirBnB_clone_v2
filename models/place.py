#!/usr/bin/python3
""" To define place class """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, Float
from sqlalchemy import ForeignKey
from models.city import City
from models.user import User


class Place(BaseModel, Base):
    """ Defining a place class """
    """"
    __tablename__ = 'palces'
    
    city_id = Column(
        String(60), ForeignKey('cities.id', ondelete="CASCADE"),
        nullable=False
        )
        
    user_id = Column(
        String(60), ForeignKey('users.id', ondelete="CASCADE"),
        nullable=False
        )
    
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    """
    __tablename__ = "places"
    city_id = Column(String(60),
                     ForeignKey("cities.id", ondelete="CASCADE"),
                      nullable=False)
    user_id = Column(String(60),
                     ForeignKey("users.id", ondelete="CASCADE"),
                     nullable=False)
    name = Column(String(128),
                  nullable=False)
    description = Column(String(1024),
                         nullable=True)
    number_rooms = Column(Integer,
                          default=0,
                          nullable=False)
    number_bathrooms = Column(Integer,
                              default=0,
                              nullable=False)
    max_guest = Column(Integer,
                       default=0,
                       nullable=False)
    price_by_night = Column(Integer,
                            default=0,
                            nullable=False)
    latitude = Column(Float,
                      nullable=True)
    longitude = Column(Float,
                       nullable=True)
