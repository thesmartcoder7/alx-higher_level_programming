#!/usr/bin/python3
"""
Adds the State object 'Louisiana' to a database and prints its assigned ID.
"""

# Import the necessary modules from the SQLAlchemy library
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    """
    Add the State object 'Louisiana' to a database and print its assigned ID.
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

    # Create a new State object named 'Louisiana' and add it to the session
    new_state = State(name="Louisiana")
    session.add(new_state)

    # Query the State object with the name 'Louisiana' to retrieve its ID
    state = session.query(State).filter_by(name="Louisiana").first()

    # Print the assigned ID of the 'Louisiana' State object
    print(str(state.id))

    # Commit changes to the database and close the session
    session.commit()
    session.close()
