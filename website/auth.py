from flask import Blueprint, render_template, redirect, request, url_for, flash, session
from website import db
from website.datamodel import User
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')  
        password = request.form.get('password') 
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                session['user_id'] = user.id
                return redirect(url_for('view.home'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('Email does not exist', category='error')
    return render_template("login.html")


@auth.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/login')

@auth.route('/login#', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('sign_user')  
        password = request.form.get('sign_pass')  
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')
        else:
            new_user = User(username=username, email=email, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created', category='success')
        
    return render_template("login.html")
