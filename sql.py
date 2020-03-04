from app import create_app
from models import db
from models.user import UserModel
from models.face import FaceModel
db.create_all(app=create_app())
