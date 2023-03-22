#!/usr/bin/python3
""" To define user class """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import environ

class User(BaseModel, Base):
    """ A user class """
    
    __tablename__ = 'users'
    
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
