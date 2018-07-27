from flask import request
from flask_restplus import Namespace, Resource, fields
# from app.api import api
from app.prasha.models import Mediums


# ns = api.namespace('prasha/mediums', description='Operations related to mediums')
ns = Namespace('prasha/mediums', description='Operations related to mediums')

model = ns.model('Medium', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a blog category'),
    'name': fields.String,
    'url': fields.String,
    # 'uri': fields.Url('api.article_item'),
})


@ns.route('/')
class MediumsList(Resource):
    model = model.inherit('Medium', {
        'uri': fields.Url('api.medium_item', absolute=True),
    })

    @ns.marshal_list_with(model)
    def get(self):
        return Mediums.query.all()

    # @api.response(201, 'Article successfully created.')
    # @api.expect(category)
    # def post(self):
    #     """
    #     Creates a new blog category.
    #     """
    #     data = request.json
    #     create_article(data)
    #     return None, 201


@ns.route('/<int:id>', endpoint='medium_item')
class MediumItem(Resource):

    @ns.marshal_list_with(model)
    def get(self, id):
        return Mediums.query.filter(Mediums.id == id).one()
