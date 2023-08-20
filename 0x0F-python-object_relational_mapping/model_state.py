#!/usr/bin/python3
"""
This script defines a SQLAlchemy model for representing states.
"""

# Import the necessary modules from the SQLAlchemy library
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative models using SQLAlchemy
Base = declarative_base()


class State(Base):
    """
    A class representing a state.

    This class is a SQLAlchemy model that defines the structure and properties of a state entity.

    Attributes:
        __tablename__ (str): The name of the database table for storing state records.
        id (int): The primary key of the state record.
        name (str): The name of the state.

    Note:
        The class definition maps this model to the "states" table in the database.
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    """
    The primary key of the state record.
    
    Type: int
    """

    name = Column(String(128), nullable=False)
    """
    The name of the state.
    
    Type: str
    """
