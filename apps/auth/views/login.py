from flask import (render_template, request, redirect, url_for)
from flask.views import MethodView
from flask_login import (current_user)

from src.databases import ad
from ..forms import LoginForm
from ..models import User


class LoginView(MethodView):
    """Login view"""

    def get(self):
        form = LoginForm(request.form)
        # Redirect to main page if user is authenticated
        if current_user.authenticated:
            return redirect(url_for('landing.index'))

        return render_template('login.html', form=form)

    def post(self):
        form = LoginForm(request.form)
        # Check form and data validate
        if not form.validate_on_submit():
            return render_template('login.html', form=form, errors=form.errors)
        if not ad.login_user(form.email.data, form.password.data):
            return render_template('login.html', form=form, errors='არასწორი მონაცემები')

        user = User.query.filter(User.email == form.email.data).first()
        if not user:
            return render_template('login.html', form=form, errors='არ გაქვთ შესვლის უფლება')
        # Update user preferences
        user.login()

        return redirect(url_for('landing.index'))
