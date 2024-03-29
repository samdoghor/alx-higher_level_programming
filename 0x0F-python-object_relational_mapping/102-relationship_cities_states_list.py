#!/usr/bin/python3
""" 0x0F-python-object_relational_mapping """

from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from relationship_city import City
from relationship_state import State

if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State)\
        .join(State, State.id == City.state_id)\
            .order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, state.name))
