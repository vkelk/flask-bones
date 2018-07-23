from app.database import db


class Medium(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    url = db.Column(db.String())
    medium_type = db.Column(db.Integer)
    is_active = db.Column(db.Boolean)
    charset = db.Column(db.String(8), default='utf-8')
    language = db.Column(db.String(2), default='mk')
