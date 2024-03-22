#!/usr/bin/python3

""" 12-model_state_update_id_2.py """


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

rename_state = session.query(State) \
    .filter(State.id == 2).first()
rename_state.name = 'New Mexico'
session.commit()

session.close()
