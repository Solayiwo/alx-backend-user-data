#!/usr/bin/env python3
"""
Module defining the User SQLAlchemy model.

This module contains the definition for the `User` class, which represents
the `users` table in the database. The model includes attributes for user
authentication and session management.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Base class for declarative class definitions
Base = declarative_base()


class User(Base):
    """
    User class to map to the `users` table in the database.

    Attributes:
        id (int): The primary key of the user table.
        email (str): The email of the user. Cannot be null.
        hashed_password (str): The hashed password of the user. Cannot be null.
        session_id (str): The session ID associated with the user. Can be null.
        reset_token (str): The reset token for password recovery. Can be null.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
