from flask import render_template
from flask_login import login_required

from app.prasha import prasha


@prasha.route('/news', methods=['GET'])
@login_required
def news():
    """Returns the applications index page."""
    return render_template('news.html')
