#!/usr/bin/python3
"""
Changes the name of the State object with id=2 to 'New Mexico' in the database.
"""

# Import the necessary modules from the SQLAlchemy library
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    """
    Change the name of the State object with id=2 to 'New Mexico' in the database.
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

    # Query the State object with id=2
    state = session.query(State).filter_by(id=2).first()

    # Check if the State object was found
    if state:
        # Update the name of the State object to 'New Mexico'
        state.name = "New Mexico"
        session.commit()
        print("State with id=2 has been updated to 'New Mexico'.")
    else:
        print("State with id=2 not found.")

    # Close the session when done
    session.close()
