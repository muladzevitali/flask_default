from flask import (render_template, request)
from flask.views import MethodView
from flask_login import (login_required, current_user)

from ..forms import SearchWord


class EmployeeDefaultInformation(MethodView):
    """View for employee default page"""
    decorators = [login_required]

    def get(self):
        form = SearchWord(request.form)
        return render_template('employee.html', user=current_user, form=form)
