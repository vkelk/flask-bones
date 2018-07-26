from app.api import api
from flask_restplus import Resource, fields
from app.prasha.models import Mediums, Articles


@api.route('/mediums')
class MediumsSchema(Resource):
    model = api.model('Medium', {
        'id': fields.Integer,
        'name': fields.String,
        'url': fields.String,
    })

    @api.marshal_with(model, envelope='resource')
    def get(self, **kwargs):
        return Mediums.query.all()


@api.route('/articles')
class ArticlesSchema(Resource):
    model = api.model('Article', {
        'id': fields.Integer,
        'medium_id': fields.Integer,
        'title': fields.String,
        'date_time': fields.DateTime(),
        'medium': fields.Nested(MediumsSchema.model)
    })

    @api.marshal_with(model, envelope='resource')
    def get(self, **kwargs):
        return Articles.query.all()


@api.route('/articles/<int:id>')
@api.response(404, 'Article not found.')
class ArticleItemSchema(Resource):

    @api.marshal_with(ArticlesSchema.model)
    def get(self, id):
        return Articles.query.filter(Articles.id == id).one()