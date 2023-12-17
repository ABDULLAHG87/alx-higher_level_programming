#!/usr/bin/python3
"""
Task 10: A Script that lists the State object with the name passed as argument from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    #creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    #declaring a boolean to detect present of name"
    match = sys.argv[4]
    result = session.query(State).filter(name = match).first()

    # check if the state was found
    if result:
        print(result.id)
    else:
        print("Not found")
    # close session
    session.close()
