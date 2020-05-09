from flask import render_template
from flask.views import MethodView
from flask_login import (login_required, current_user)


class LandingIndex(MethodView):
    """Index Page View"""
    decorators = [login_required]

    def get(self):
        return render_template('index.html', user=current_user)
