#!/usr/bin/python3
"""
Creates the State 'California' with the City 'San Francisco' in the database.
"""

# Import the necessary modules from the SQLAlchemy library
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv

if __name__ == "__main__":
    """
    Create the State 'California' with the City
    'San Francisco' in the database.
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

    # Create a new State object named 'California' and add it to the session
    cali = State(name="California")

    # Create an object named 'San Francisco' and associate it with 'California'
    san_francisco = City(name="San Francisco")
    cali.cities = [san_francisco]

    # Add the State and City objects to the session and commit changes to db
    session.add(cali)
    session.commit()

    # Close the session when done
    session.close()
