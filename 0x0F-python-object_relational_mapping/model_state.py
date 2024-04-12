#!/usr/bin/python3
"""the begining of the SQLALCHEMY"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, MetaData

mymetadata = MetaData()
Base = declarative_base()

class State(Base):
    """
    Class with id and name
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)