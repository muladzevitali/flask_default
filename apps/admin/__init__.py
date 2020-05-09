from flask_admin import Admin

from .model_views import (IndexView, RoleView, UserView)
from apps import db
from apps.auth.models import (User, Role)

admin_app = Admin(endpoint='admin', index_view=IndexView(url="/admin"), template_mode='bootstrap3')
admin_app.add_view(UserView(User, db.session, name='Users'))
admin_app.add_view(RoleView(Role, db.session, name='Roles'))
