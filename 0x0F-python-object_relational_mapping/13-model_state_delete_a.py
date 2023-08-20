#!/usr/bin/python3
"""
This script changes the name of the State object with id=2 to
"New Mexico" in a database.
"""

# Import necessary modules
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    """
    Main script to change the name of a State object in the database.
    """
    # Create a database engine using SQLAlchemy
    eng = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
    )

    # Create the database tables if they don't exist
    Base.metadata.create_all(eng)

    # Create a session to interact with the database
    Session = sessionmaker(bind=eng)
    session = Session()

    # Query for State objects with names containing "a"
    states = session.query(State).filter(State.name.like("%a%"))

    # Iterate through the queried states and delete them
    for state in states:
        session.delete(state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
