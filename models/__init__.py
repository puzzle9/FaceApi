from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Mixin:
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self, data=[]):
        if data:
            for info in data:
                db.session.delete(info)
        else:
            db.session.delete(self)

        db.session.commit()
        return self

    def commit(self):
        db.session.commit()
        return self
