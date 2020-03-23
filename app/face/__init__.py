from flask import Blueprint

blueprint = Blueprint('face', __name__, url_prefix='/face')

from . import face
