from flask import Blueprint, current_app
from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound

from app.api.prasha.endpoints.articles import ns as articles_ns
from app.api.prasha.endpoints.mediums import ns as mediums_ns

api_bp = Blueprint('api', __name__)
api = Api(api_bp, version='1.0', title='Prasha API', ordered=True)
api.add_namespace(articles_ns)
api.add_namespace(mediums_ns)


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    # log.exception(message)

    if not current_app.config['FLASK_DEBUG']:
        return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    # log.warning(traceback.format_exc())
    return {'message': 'A database result was required but none was found.'}, 404
