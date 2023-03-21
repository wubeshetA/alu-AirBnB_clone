#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
# import sqlalchemy modules
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):

    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")