from datetime import datetime
import secrets
import string
from app.database import db


class Mediums(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    url = db.Column(db.String(), nullable=False, unique=True)
    medium_type = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    charset = db.Column(db.String(8), default='utf-8')
    language = db.Column(db.String(2), default='mk')


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medium_id = db.Column(db.Integer, db.ForeignKey('mediums.id'), nullable=False)
    url = db.Column(db.String(512), nullable=False, unique=True)
    category = db.Column(db.String(60))
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    md5hash = db.Column(db.String(32), nullable=False, unique=True)
    date_time = db.Column(db.DateTime, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)


class ArticleMedia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'), nullable=False)
    media_type = db.Column(db.String(15), nullable=False)
    media_url = db.Column(db.String(1024), nullable=False)


class ArticleTags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'), nullable=False)
    tag = db.Column(db.String(), nullable=False)


class Clients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    phone = db.Column(db.String(30))
    address = db.Column(db.String())
    is_active = db.Column(db.Boolean, default=True)
    auth_key = db.Column(db.String(),
                         default=''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(5)))
    created = db.Column(db.DateTime, default=datetime.utcnow)


class ClientKeywords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    keyword = db.Column(db.String())
    keyword_wight = db.Column(db.Integer)


class UserClients(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    is_authorized = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow)
