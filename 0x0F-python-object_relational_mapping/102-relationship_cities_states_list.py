#!/usr/bin/python3
"""
Lists all City objects from a database.
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv

if __name__ == "__main__":
    """
    Retrieve and display information about City objects from a database.
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

    # Retrieve all City objects from the database
    cities = session.query(City).all()

    # Display information about each City object
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close the session when done
    session.close()
