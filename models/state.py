#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models import storage
from models.base_model import BaseModel, Base, City
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ represents a `State` and
    maps to the table `states`"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list