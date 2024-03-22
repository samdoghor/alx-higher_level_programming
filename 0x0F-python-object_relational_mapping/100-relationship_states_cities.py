#!/usr/bin/python3
""" 0x0F-python-object_relational_mapping """

from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = State(name="California")

    session.add(new_state)
    session.commit()

    new_city = City(name="San Francisco", state_id=new_state.id)

    session.add(new_city)
    session.commit()
    session.close()
