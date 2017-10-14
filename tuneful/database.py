from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey

from . import app

engine = create_engine(app.config["DATABASE_URI"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Create your models here / if we don't add models here, it doesn't generate the db

# since it's good practice to have all models in their own file(since this files handles connection to db)
# we just import it
from . import models


Base.metadata.create_all(engine)
