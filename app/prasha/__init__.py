from flask import Blueprint

prasha = Blueprint('prasha', __name__, template_folder='templates')

from .views import news, archive, clipping, analysis
