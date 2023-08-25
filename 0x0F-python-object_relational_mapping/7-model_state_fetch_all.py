#!/usr/bin/python3
'''
Script that lists all states Object from the database htbn_0e_6_usa
Module: SQLAlchemy

'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from  model_state import Base, State

if __name__ == "__main__":
    conn_string = "mysql+mysqldb://{}:{}@localhost/{}"
                    .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    engine = create_engine(conn_string)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name})
