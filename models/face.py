from flask import current_app, abort
from datetime import datetime
from . import db, Mixin
from utils.pickle import PickleDumps, PickleLoads


class FaceModel(db.Model, Mixin):
    __tablename__ = 'faces'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    degree = db.Column(db.Float)
    data = db.Column(db.LargeBinary)
    create_time = db.Column(db.DateTime, default=datetime.now)


def FaceAdd(user_id, data, degree):
    face = FaceModel(
        user_id=user_id,
        data=PickleDumps(data),
        degree=degree,
    )
    return face.save()


def FaceDatas(user_id):
    from models.user import UserGet

    degree = current_app.config['FACE_TOLERANCE']

    data =  FaceModel().query.filter(
        FaceModel.user_id == user_id,
        FaceModel.degree <= degree
    ).order_by(FaceModel.create_time.desc()).limit(30).all()

    datas = []
    for info in data:
        datas.append(PickleLoads(info.data))

    userData = UserGet(user_id).data
    if not userData:
        abort(422, 'no default img')

    return [PickleLoads(userData)] + datas


def FaceDelete(user_id):
    lists = FaceModel().query.filter_by(user_id=user_id).all()
    if lists:
        FaceModel().delete(lists)
