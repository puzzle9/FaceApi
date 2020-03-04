from functools import wraps
from flask import request, abort


def check(user_id=True, file=False):
    def decorator(f):
        @wraps(f)
        def body(*args, **kwargs):
            if user_id:
                if not  request.form.get('user_id') and not request.args.get('user_id'):
                    abort(422, 'no user_id')

            if file:
                if not  request.files.get('file'):
                    abort(422, 'no file')

            return f(*args, **kwargs)
        return body
    return decorator
