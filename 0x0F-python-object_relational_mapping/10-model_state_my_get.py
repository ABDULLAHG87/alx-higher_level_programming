#!/usr/bin/python3
"""
Task 10: A Script that lists the State object with the name passed.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # declaring a boolean to detect present of name"
    found = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = True
            break

    # check if the state was found
    if found is False:
        print("Not found")
    # close session
    session.close()
