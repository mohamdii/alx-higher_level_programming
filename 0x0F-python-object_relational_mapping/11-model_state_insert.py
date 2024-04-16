#!/usr/bin/python3
"""the last one before i go to bed"""
import sys
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == '__main__':
    conD = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(conD.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    newUser = State(name='Luisiana')
    session.add(newUser)
    session.commit()

    print(newUser.id)
