from flask import Flask
from  models import db
from .blueprint import register_blueprints
from .error import  register_errors

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    register_blueprints(app)
    register_errors(app)

    return app
