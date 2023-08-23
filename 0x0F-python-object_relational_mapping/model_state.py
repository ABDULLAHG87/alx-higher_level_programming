#!/usr/bin/python3
'''
create a file that contains the class definition of a state 
'''

from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    '''
    A class that inherits from the declarative base to represetn as state
    for MySQL database
    PROPERTIES:
          __tablename__(str) stores the name of the table states
          id: Integer, primary key
          name: String of size 128
    '''

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
