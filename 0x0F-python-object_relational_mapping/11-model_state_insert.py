#!/usr/bin/python3
""" 11-model_state_insert.py """


import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]),
    pool_pre_ping=True)

Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

session = Session()

new_state = State(name='Louisiana')
session.add(new_state)
session.commit()

state_add = session.query(State).filter(State.name == 'Louisiana').one()
print(state_add.id)

session.close()
