#!/usr/bin/python3

"""
Statements
"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import (create_engine)


def conect():
    """Connection to database"""
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                               format(
                                   argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(engine)
    except Exception:
        print("No se puede conectar")
        return 0

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    new_state.cities = [City(name="San Francisco")]
    session.add(new_state)
    session.commit()

    session.close()


if __name__ == "__main__":
    conect()
