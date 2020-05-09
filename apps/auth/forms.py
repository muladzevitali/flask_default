from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import (validators, PasswordField)


class LoginForm(FlaskForm):
    email = StringField("email", validators=[validators.required(message='გთხოვთ შეავსოთ ველი')])
    password = PasswordField("password", validators=[validators.length(min=8)])

    def validate_email(self, field):
        email = field.data

        if "@bog.ge" not in email:
            email = email + "@bog.ge"
        self.email.data = email
