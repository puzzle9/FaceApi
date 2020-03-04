from app.response import error


def register_errors(app):
    @app.errorhandler(422)
    def errorhandler_422(err):
        return error(err.description)

