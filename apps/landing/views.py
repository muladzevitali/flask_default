from flask import (Blueprint, redirect, url_for, render_template, request)
from flask_login import (login_required, current_user)

from apps.employee.forms import SearchWord

landing_app = Blueprint('landing', __name__, template_folder='templates',
                        static_folder='statics', static_url_path='/statics/landing')


@landing_app.route('/')
@login_required
def index():
    form = SearchWord(request.form)
    return render_template('index.html', user=current_user, form=form)


@landing_app.route('/favicon.ico')
def favicon():
    return redirect(url_for('landing.static', filename='images/favicon.png'))
