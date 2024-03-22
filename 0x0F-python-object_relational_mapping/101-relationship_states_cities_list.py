#!/usr/bin/python3
"""List all states"""
from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from relationship_state import State
from relationship_city import City

engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost/{}'
    .format(argv[1], argv[2],
            argv[3]), pool_pre_ping=True)

Session = sessionmaker(bind=engine)
session = Session()

for state in session.query(State).order_by(State.id):
    print("{}: {}".format(state.id, state.name))
    for city in state.cities:
        print("\t{}: {}".format(City.id, City.name))
