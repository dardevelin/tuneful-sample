import os.path
import json

from flask import request, Response, url_for, send_from_directory, redirect
from werkzeug.utils import secure_filename
from jsonschema import validate, ValidationError

from . import decorators
from . import app
from .database import session
from . import models
from .utils import upload_path


@app.route("/api/songs", methods=["GET"])
@decorators.accept("application/json")
def song_get():
    songs = session.query(models.Song).all()
    if not songs:
        data = None
        return Response(json.dumps(data), 404, mimetype="application/json")

    data = [ song.as_dictionary() for song in songs]
    data = json.dumps(data)
    
    return Response(data, 200, mimetype="application/json")


@app.route("/api/files", methods=["POST"])
@decorators.require("multipart/form-data")
@decorators.accept("application/json")
def file_post():
    file = request.files.get("file")
    if not file:
        data = {"message": "Could not find file data"}
        return Response(json.dumps(data), 422, mimetype="application/json")

    filename = secure_filename(file.filename)
    db_file = models.File(filename=filename)
    session.add(db_file)
    session.commit()
    file.save(upload_path(filename))

    data = db_file.as_dictionary()
    return Response(json.dumps(data), 201, mimetype="application/json")

@app.route("/api/songs", methods=["POST"])
@decorators.accept("application/json")
def song_post():
    # use utf8 to re-interpret the binary data
    # provided by request.data as a string
    # since it is a string but formated as a dictionary, we can use
    # json.loads which reads a string and returns a dictionary of that obj
#    print(request.data)
#    print(request.data.decode('utf-8'))
    obj = json.loads(request.data.decode('utf-8'))
#    print(obj)
#    print(obj['file'])
#    print(obj['file']['id'])

    # now that we have a dictionary we can just access it

    song = models.Song(file=obj['file']['id'])
    session.add(song)
    session.commit()

    data = song.as_dictionary()
    return Response(json.dumps(data), 201, mimetype="application/json")


# this is actually what sends the music to the browser
@app.route("/uploads/<filename>", methods=["GET"])
def uploaded_file(filename):
    return send_from_directory(upload_path(), filename)
