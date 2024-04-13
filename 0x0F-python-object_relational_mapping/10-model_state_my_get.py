#!/usr/bin/python3
"""name passed as an argument"""
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
    instance = session.query(State).filter(State.name == sys.argv[4]).first()
    
    if instance:
        print(instance.id)
