from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, abort
from models import db, User
from flask_migrate import Migrate
from forms import LoginForm

app = Flask(__name__)
app.secret_key = 'As12@#!$%wrwedsfwq!#$#@aghbnnjk!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/registration')
def registration():
    users = User.query.all()
    return render_template('registration.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)





