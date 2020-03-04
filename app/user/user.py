from flask import request
from . import blueprint
from models.user import UserCreate, UserUpdate, UserEmpty, UserDeleteFaces
from utils.face import FaceEncodings
from app.check import check
from app.response import success


@blueprint.route('/create', methods=['POST'])
def create():
    info = UserCreate()
    return success({
        'user_id': info.id,
    })


@blueprint.route('/empty', methods=['DELETE'])
@check(file=False)
def empty():
    UserEmpty(request.args.get('user_id'))
    return success();


@blueprint.route('/face/update', methods=['POST'])
@check(file=False)
def faceAdd():
    user_id = request.form.get('user_id')
    file = request.files.get('file')

    if file:
        data = FaceEncodings(file)
    else:
        data = None

    UserUpdate(user_id, data)

    return success()


@blueprint.route('/face/delete', methods=['DELETE'])
@check(file=False)
def delete():
    UserDeleteFaces(request.args.get('user_id'))
    return success();
