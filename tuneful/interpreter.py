# proof of concept, how to test in the interpreter if the models work
#imports here first
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey

#connection to db
engine = create_engine("postgresql://ubuntu:thinkful@localhost:5432/tuneful-pa")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

#models design
class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True)
    file = Column(Integer, ForeignKey("files.id"))

    def as_dictionary(self):
        ret = { "id":self.id,
                "file": {
                    "id": self.song.id,
                    "name":self.song.filename
                    }
                }

        return ret

    def __repr__(self):
        return str(self.as_dictionary())

class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True)
    filename = Column(String(1024))
    song = relationship("Song", backref="song")

    def as_dictionary(self):
        return { "id":self.id, "name": self.filename}

# create the db based on this models
Base.metadata.create_all(engine)


# print data of this database
