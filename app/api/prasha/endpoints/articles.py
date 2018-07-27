from flask import request
from flask_restplus import Namespace, Resource, fields
# from app.api import api
from app.prasha.models import Articles
from .mediums import MediumsList

# ns = api.namespace('prasha/articles', description='Operations related to articles')
ns = Namespace('prasha/articles', description='Operations related to articles')

model = ns.model('Article', {
        'id': fields.Integer(readOnly=True, description='The unique identifier of a blog category'),
        'medium_id': fields.Integer,
        'title': fields.String(required=True, description='Article title'),
        'date_time': fields.DateTime(),
        'medium': fields.Nested(MediumsList.model),
    })


@ns.route('/')
class ArticlesList(Resource):
    model = model.inherit('Article', {
        'uri': fields.Url('api.article_item', absolute=True),
    })

    @ns.marshal_list_with(model)
    def get(self):
        return Articles.query.all()

    # @api.response(201, 'Article successfully created.')
    # @api.expect(category)
    # def post(self):
    #     """
    #     Creates a new blog category.
    #     """
    #     data = request.json
    #     create_article(data)
    #     return None, 201


@ns.route('/<int:id>', endpoint='article_item')
class ArticleItem(Resource):
    model = model.inherit('Article', {
        'body': fields.String
    })

    @ns.marshal_list_with(model)
    def get(self, id):
        return Articles.query.filter(Articles.id == id).one()
