# https://face-recognition.readthedocs.io/

from flask import abort
import face_recognition as fr
import numpy


def FaceEncodings(file):
    img = fr.load_image_file(file)
    encodings = fr.face_encodings(img)
    if not encodings:
        abort(422, 'error face img')

    return encodings[0]

def FaceDistance(face_encodings, face_to_compare):
    distances = fr.face_distance(face_encodings, face_to_compare)

    return {
        'current': distances[0],
        'mean': numpy.mean(distances),
        'count': len(face_encodings),
    }