#!/usr/bin/python3
""" Database storage module """
from sqlalchemy import create_engine
# import declarative base
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
from models.user import User

class DBStorage:

    # private class attributes
    __engine = None
    __session = None

    def __init__(self):

        # get environment variables
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        port = os.getenv('HBNB_MYSQL_PORT')
        env = os.getenv('HBNB_ENV')
        # storage_type = os.getenv('HBNB_STORAGE_TYPE')

        db_path = ('mysql+mysqldb://{}:{}@{}/{}'
                   .format(user, passwd, host, db))

        self.__engine = create_engine(db_path, pool_pre_ping=True)
        # drop all tables if the environment variable HBNB_ENV is equal to test
        if env == 'test':
            Base.metadata.drop_all(self.__engine)