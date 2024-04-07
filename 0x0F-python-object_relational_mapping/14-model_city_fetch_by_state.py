#!/usr/bin/python3

""" Select all states from database """
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    """ Main function """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    session = Session(engine)
    for city in (session.query(State.name, City.id, City.name)
                 .filter(State.id == City.state_id)):
        print("{}: ({}) {}".format(city[0], city[1], city[2]))
    session.close()
