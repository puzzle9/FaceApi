from flask import request
from . import blueprint
from utils.face import FaceEncodings, FaceDistance
from models.face import FaceAdd, FaceDatas
from app.response import success
from app.check import check


@blueprint.route('/check', methods=['POST'])
@check(file=True)
def faceCheck():
    user_id = request.form.get('user_id')
    file = request.files.get('file')

    faceEncoding = FaceEncodings(file)
    face_encodings = FaceDatas(user_id)
    distances = FaceDistance(face_encodings, faceEncoding)

    FaceAdd(user_id, faceEncoding, distances['current'])

    return success(distances)
