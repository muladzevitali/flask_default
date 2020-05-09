from flask import (session, request, redirect, url_for)
from flask_admin.babel import gettext
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class UserView(ModelView):
    """Class for Admin models view"""
    logger_collection = 'requests'
    column_list = ('first_name', 'last_name', 'email', 'manager', 'authenticated', 'active')
    column_labels = dict(first_name='სახელი',
                         last_name='გვარი',
                         email='მაილი',
                         manager='მენეჯერი',
                         authenticated='ავტორიზებული',
                         active='აქტიური')
    can_delete = False

    def is_accessible(self):
        if current_user.has_role("admin"):
            return True

        return False

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        session["next_url"] = request.endpoint

        return redirect(url_for('landing.index'))

    def get_empty_list_message(self):
        return gettext('ჩანაწერი არ მოიძებნა')
