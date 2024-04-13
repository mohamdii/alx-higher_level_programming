#!/usr/bin/python3
"""Still learning bs"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys
if __name__ == '__main__':
    conD = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(conD.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).filter(State.name.like('%a%')):
        print(instance.id, instance.name, sep=': ')
