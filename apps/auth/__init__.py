from flask import Blueprint

from .views import (LoginView, LogoutView)

auth_app = Blueprint(name='auth', import_name=__name__, static_folder='statics', static_url_path='/statics/auth',
                     template_folder='templates', url_prefix='/auth')

auth_app.add_url_rule('/login', view_func=LoginView.as_view('login'))
auth_app.add_url_rule('/logout', view_func=LogoutView.as_view('logout'))
