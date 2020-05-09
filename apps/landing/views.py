from flask import (Blueprint, redirect, url_for, render_template, request)
from flask_login import (login_required, current_user)


landing_app = Blueprint('landing', __name__, template_folder='templates',
                        static_folder='statics', static_url_path='/statics/landing')


@landing_app.route('/')
@login_required
def index():
    return render_template('index.html', user=current_user)


@landing_app.route('/favicon.ico')
def favicon():
    return redirect(url_for('landing.static', filename='images/favicon.png'))
