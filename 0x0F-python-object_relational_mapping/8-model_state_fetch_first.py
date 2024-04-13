#!/usr/bin/python3
"""SQLALCHEMY ORM expert"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
if __name__ == "__main__":
    conD = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(conD.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).first()
    if instance is None:
        print('Nothing')
    else:
        print(instance.id, instance.name, sep=': ')
