#!/usr/bin/python3
"""
Prints all City objects from a database along with their
associated State names.
"""

# Import the necessary modules from the SQLAlchemy library
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    """
    Print all City objects from a database along with their
    associated State names.
    """
    # Create a database connection using SQLAlchemy's create_engine function
    eng = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
    )

    # Create the tables in the database based on the defined models
    Base.metadata.create_all(eng)

    # Create a session to interact with the database
    Session = sessionmaker(bind=eng)
    session = Session()

    # Retrieve City objects along with their associated State names
    rows = (
        session.query(City, State)
        .filter(City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    # Print information about each City object and its associated State name
    for city, state in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session when done
    session.close()
