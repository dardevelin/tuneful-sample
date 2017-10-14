# for our models to work we need to have the connection to the db
from .database import *
# url_for will be needed to be able to provide the physical location of the file
from flask import url_for

# defines what a song is (as data, but not the actual file that contains the audio)
class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True)
    file = Column(Integer, ForeignKey("files.id"))

    def as_dictionary(self):
        return { "id":self.id, "file": { "id": self.song.id, "name":self.song.filename, "path": url_for('uploaded_file', filename=self.song.filename) } }

# defines what the actual audio data is(by location and name, but not the metadata)
class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True)
    filename = Column(String(1024))
    song_id = relationship("Song", backref="song")

    def as_dictionary(self):
        return { "id":self.id, "name": self.filename }

# both of this classes need each other, since Song depends on a file existing for it to make sense
# our application always creates a File first and then a Song metadata
