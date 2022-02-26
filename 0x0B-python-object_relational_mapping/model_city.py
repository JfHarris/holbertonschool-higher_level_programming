#!/usr/bin/python3
"""
contains the class definition of a City
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base

Base = declarative_base()


class City(Base):
    """
    inherits from Base (imported from model_state)
    links to the MySQL table cities
    id = a column auto-generated unique int never null is primary key
    name = a column of a string of 128 chars and cant be null
    state_id = a column of an int, never null and is foreign key to states.id
    """

    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, foreign_key='states.id')
