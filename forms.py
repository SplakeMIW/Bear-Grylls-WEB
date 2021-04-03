from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Email, DataRequired, EqualTo
from wtforms.widgets import PasswordInput

class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = StringField(label="Пароль", widget=PasswordInput(), validators=[DataRequired()])

class RegistrationForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    nickname = StringField(label="Никнейм", validators=[DataRequired()])
    password = StringField(label="Пароль", widget=PasswordInput(), validators=[DataRequired(),
                                        EqualTo('confirmation', message="Пароли должны совпадать")])
    confirmation = StringField(label="Подтвердите пароль", widget=PasswordInput(), validators=[DataRequired()])