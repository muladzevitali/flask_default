from flask import (Blueprint, redirect, url_for)

from .views import LandingIndex

landing_app = Blueprint('landing', __name__, template_folder='templates',
                        static_folder='statics', static_url_path='/statics/landing')

landing_app.add_url_rule('/', view_func=LandingIndex.as_view('index'))


@landing_app.route('/favicon.ico')
def favicon():
    return redirect(url_for('landing.static', filename='images/favicon.png'))
