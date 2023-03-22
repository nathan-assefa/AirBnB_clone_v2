#!/usr/bin/python3
""" To define place class """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, Float
from sqlalchemy import ForeignKey
from models.city import City
from models.user import User
from sqlalchemy.orm import relationship
from os import eviron


class Place(BaseModel, Base):
    """ Defining a place class """

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
    
    if environ['HBNB_TYPE_STORAGE'] == 'db':
        reviews = relationship(
                'Review', cascade='all, delete', backref='place'
                )
    else:
        @property
        def reviews():
            from models import storage
            all_reviews = storage.all(Review)
            filtered_reviews = []

            for rev in all_reviews.values():
                if rev.plae_id == self.id:
                    filtered_reviews.append(rev)
            return filtered_reviews
