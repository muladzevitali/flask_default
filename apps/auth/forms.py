from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import (validators, PasswordField)


class LoginForm(FlaskForm):
    email = StringField("email", validators=[validators.required(message='Please fill the field')])
    password = PasswordField("password", validators=[validators.length(min=5)])
