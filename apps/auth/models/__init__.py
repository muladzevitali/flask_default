from flask import (redirect, url_for)
from flask_login import current_user

from .roles import Role
from .users import (User, AnonymousUser)
from .users_roles_rel import UserRoleRel


def user_loader(username):
    """User loader for flask login"""
    return User.query.filter_by(username=username).first()


def unauthorized():
    """Unauthorized handler for flask_login"""
    if not current_user.authenticated:
        return redirect(url_for("auth.login"))
    return redirect(url_for("landing.index"))
