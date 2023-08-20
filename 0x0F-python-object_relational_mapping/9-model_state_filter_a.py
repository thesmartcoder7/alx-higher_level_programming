#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from a database.
"""

# Import the necessary modules from the SQLAlchemy library
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    """
    List all State objects that contain the letter 'a' from a database.
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

    # Define the pattern containing the letter 'a'
    s = "%a%"

    # Query State objects that contain the letter 'a' in their names
    states = session.query(State).filter(State.name.like(s)).order_by(State.id)

    # Iterate through the queried State objects and print their information
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session when done
    session.close()
