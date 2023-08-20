#!/usr/bin/python3
"""
Prints the State object with the name passed as an argument from a database.
"""

# Import the necessary modules from the SQLAlchemy library
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    """
    Print the State object with the name passed as an argument from a database.
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

    # Query the State object with the name passed as an argument
    state = session.query(State).filter_by(name=argv[4]).first()

    # Check if the State object with the given name was found
    if state is not None:
        # Print the ID of the found State object
        print(str(state.id))
    else:
        print("Not found")

    # Close the session when done
    session.close()
