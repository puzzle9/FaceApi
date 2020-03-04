import os

DEBUG = False
SQLALCHEMY_ECHO = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.abspath('db.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# https://face-recognition.readthedocs.io/en/latest/face_recognition.html#face_recognition.api.compare_faces
# How much distance between faces to consider it a match. Lower is more strict.
FACE_TOLERANCE = '0.35'
