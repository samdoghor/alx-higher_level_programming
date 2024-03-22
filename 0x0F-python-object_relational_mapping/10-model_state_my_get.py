#!/usr/bin/python3
""" 10-model_state_my_get.py """


import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()

    states = session.query(State) \
                    .filter(State.name == sys.argv[4]).one_or_none()

    if states is None:
        print("Not found")
    else:
        print(states.id)

    session.close()
