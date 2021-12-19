#!/usr/bin/python3

"""
Statements
"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

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

    first_e = session.query(State.id, State.name).first()
    if first_e is not None:
        print("{}: {}".format(first_e.id, first_e.name))
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    conect()