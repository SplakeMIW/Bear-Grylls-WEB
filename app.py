from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, abort, redirect, url_for
from models import db, User
from flask_migrate import Migrate
from forms import RegistrationForm, LoginForm
from flask_login import login_user, LoginManager

app = Flask(__name__)
app.secret_key = 'As12@#!$%wrwedsfwq!#$#@aghbnnjk!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)


@login_manager.user_loader()
def user_loader(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            abort(400)
        nickname = form.nickname.data
        user = User(email=email,nickname=nickname)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)
        return redirect(url_for('homepage'))
    return render_template('registration.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)






