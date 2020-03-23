from app import create_app as _create_app

app = _create_app()

def create_app():
    return app

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5050')