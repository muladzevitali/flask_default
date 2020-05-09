from flask_wtf import FlaskForm
from wtforms import (StringField, validators)


class SearchWord(FlaskForm):
    search_word = StringField("search_word", validators=[validators.required(message='გთხოვთ შეავსოთ ველი')])
