from flask import  abort
from . import db, Mixin
from utils.pickle import PickleDumps


class UserModel(db.Model, Mixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.LargeBinary, nullable=True)
    # faces = db.relationship('FaceModel', lazy='dynamic' )


def FaceDelete(user_id):
    from models.face import  FaceDelete
    FaceDelete(user_id)


def UserGet(user_id):
    user = UserModel().query.get(user_id)
    if not user:
        abort(422, 'no user')
    return  user


def UserCreate(user_id):
    if user_id:
        user = UserModel().query.get(user_id)
        if user:
            abort(422, 'have user_id')

    user = UserModel()
    user.id = user_id
    return user.save()


def UserUpdate(user_id, info):
    user = UserGet(user_id)
    print(type(info))
    if info is None:
        data = None
    else:
        data = PickleDumps(info)

    user.data = data
    return user.commit()


def UserEmpty(user_id):
    FaceDelete(user_id)
    UserModel.delete(UserGet(user_id))


def UserDeleteFaces(user_id):
    FaceDelete(user_id)