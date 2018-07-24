from datetime import datetime
from app.database import db


class Mediums(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    url = db.Column(db.String())
    medium_type = db.Column(db.Integer)
    is_active = db.Column(db.Boolean)
    charset = db.Column(db.String(8), default='utf-8')
    language = db.Column(db.String(2), default='mk')


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medium_id = db.Column(db.Integer, db.ForeignKey('mediums.id'))
    url = db.Column(db.String(512))
    category = db.Column(db.String(60))
    title = db.Column(db.Text)
    body = db.Column(db.Text)
    md5hash = db.Column(db.String(32))
    date_time = db.Column(db.DateTime)
    created = db.Column(db.DateTime, default=datetime.utcnow)


class ArticleMedia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
    media_type = db.Column(db.String(15))
    media_url = db.Column(db.String(1024))


class ArticleTags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
    tag = db.Column(db.String())


class Clients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    phone = db.Column(db.String(30))
    address = db.Column(db.String())
    is_active = db.Column(db.Boolean)
    auth_key = db.Column(db.String())
    created = db.Column(db.DateTime, default=datetime.utcnow)


class ClientKeywords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    keyword = db.Column(db.String())
    keyword_wight = db.Column(db.Integer)
