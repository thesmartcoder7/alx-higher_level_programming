#!/usr/bin/python3
"""
Lists the first State object from a database.
"""

# Import the necessary modules from the SQLAlchemy library
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    """
    List the first State object from a database.
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

    # Query and retrieve the first State object
    first_state = session.query(State).order_by(State.id).first()

    # Check if a State object was found
    if first_state is not None:
        # Print the information of the first State object
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close the session when done
    session.close()
