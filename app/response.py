from flask import jsonify


def success(info='success'):
    data = {
        'code': 200,
    }

    if isinstance(info, str):
        data['message'] = info
    else:
        data = {**data, **info}

    return jsonify(data)

def error(message):
    return jsonify({
        'code': 201,
        'message': message,
    })
