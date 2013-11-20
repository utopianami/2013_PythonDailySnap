from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from flask_login import (LoginManager, login_required, login_user, 
                         current_user, logout_user, UserMixin)


from app import db
from app.users.models import User

mod = Blueprint('users', __name__, url_prefix='/users')


@mod.route('/signUp')
def signUp():
    return render_template('signUp.html')

@mod.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']
    user = User.query.filter_by(userEmail = email).first()

    if (user): 
        return 'exist'
    else:
        newUser = User(request.form['email'], request.form['password'])
        db.session.add(newUser)
        db.session.commit()

    return redirect(url_for('index'))

@mod.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(userEmail = email).first()
        if user == None:
            return 'no exist'
        if user.userPassword == password:
            session['user'] = email
            return redirect(url_for('flow.flows'))

    return 'wrong password'