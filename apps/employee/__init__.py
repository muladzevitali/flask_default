from flask import (Blueprint)

from .views import (EmployeeDefaultInformation, EmployeeSearch)

employee_app = Blueprint('employee_app', __name__, template_folder='templates', url_prefix='/employee')

employee_app.add_url_rule('/', view_func=EmployeeDefaultInformation.as_view('default'))
employee_app.add_url_rule('/search', view_func=EmployeeSearch.as_view('search'))
