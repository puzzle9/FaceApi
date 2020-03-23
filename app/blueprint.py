def register_blueprints(app):

    from app.index import blueprint as index
    app.register_blueprint(index)

    from app.user import blueprint as user
    app.register_blueprint(user)

    from app.face import blueprint as face
    app.register_blueprint(face)

