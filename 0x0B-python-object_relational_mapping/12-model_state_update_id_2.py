#!/usr/bin/python3
"""
changes name of a State object from hbtn_0e_6_usa
"""


from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_rec = session.query(State).filter(State.id == 2).one()
    new_rec.name = "New Mexico"
    session.commit()

    session.close()
