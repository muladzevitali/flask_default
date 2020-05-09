from flask import (redirect, url_for)
from flask.views import MethodView
from flask_login import (current_user)

from ..models import User


class LogoutView(MethodView):
    """Logout view"""
    def get(self):
        user: User = current_user
        user.logout()

        return redirect(url_for('auth.login'))
