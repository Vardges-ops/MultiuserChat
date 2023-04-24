from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///events.db", echo=True)


def create_db():  # TODO find the correct usage place of this function
    Base.metadata.create_all(engine)
