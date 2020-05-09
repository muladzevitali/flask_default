from flask import (request, redirect, url_for, render_template)
from flask.views import MethodView
from flask_login import (login_required, current_user)

from src.databases import ad
from ..forms import SearchWord


class EmployeeSearch(MethodView):
    """View for Employee search"""
    decorators = [login_required]

    def get(self):
        form = SearchWord(request.form)
        search_word = request.args.get('search_word')
        search_results = ad.search(filter_string=search_word)

        return render_template('employee_list.html', search_results=search_results, form=form, user=current_user)

    def post(self):
        form = SearchWord(request.form)
        if form.validate_on_submit():
            return redirect(url_for('employee_app.search', search_word=form.search_word.data))

        return {}
