#!/usr/bin/python3
"""
This script defines a SQLAlchemy model for representing cities and their associated states.
"""

# Import the necessary modules from the SQLAlchemy library
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """
    A class representing a city.

    This class is a SQLAlchemy model that defines the structure and properties of a city entity.

    Attributes:
        __tablename__ (str): The name of the database table for storing city records.
        id (int): The primary key of the city record.
        name (str): The name of the city.
        state_id (int): The foreign key referencing the associated state's ID.

    Note:
        The class definition maps this model to the "cities" table in the database.
        This model has a foreign key relationship with the "states" table.
    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    """
    The primary key of the city record.
    
    Type: int
    """

    name = Column(String(128), nullable=False)
    """
    The name of the city.
    
    Type: str
    """

    state_id = Column(Integer, ForeignKey("states.id"))
    """
    The foreign key referencing the associated state's ID.
    
    Type: int
    """
