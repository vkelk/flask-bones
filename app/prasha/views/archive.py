from flask import render_template
from flask_login import login_required

from app.prasha import prasha


@prasha.route('/archive', methods=['GET'])
@login_required
def archive():
    """Returns the applications index page."""
    return render_template('index.html')
