#!/usr/bin/python3
'''
Script file to print state object with name passed as argument from
database
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session,sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # creating a session
    # Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(louisiana.id)

    session.close()
