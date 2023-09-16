#!/usr/bin/python3
"""class definition of a City"""


from sqlalchemy import Column, ForeignKey, Integer, String
from relationship_state import Base, State

class City(Base):
    """
    cities table:
        id: primary key
        name: name of the city
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
