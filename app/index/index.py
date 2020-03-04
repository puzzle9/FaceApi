from . import blueprint
from app.response import success
from datetime import datetime

@blueprint.route('/', methods=['GET'])
def index():
    return success({
        'time': datetime.now(),
    })