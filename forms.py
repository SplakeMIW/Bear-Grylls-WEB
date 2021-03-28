from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import Email, DataRequired
from wtforms.widgets import PasswordInput

class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = StringField(label="Пароль", widget=PasswordInput(), validators=[DataRequired()])

class RegistrationForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    nickname = StringField(label="Никнейм", validators=[DataRequired()])
    password = StringField(label="Пароль", widget=PasswordInput(), validators=[DataRequired()])
    confirmation = StringField(label="Подтвердите пароль", widget=PasswordInput(), validators=[DataRequired()])
