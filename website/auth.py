from flask import Blueprint, render_template, redirect, request, url_for, flash
from website import db
from website.datamodel import User
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')  
        password = request.form.get('password') 
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return redirect('/login')

@auth.route('/login#', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('sign_user')  
        password = request.form.get('sign_pass')  
        email = request.form.get('email')
        new_user = User(username=username, email=email, password=generate_password_hash(password, method='pbkdf2:sha256'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('view.home'))

    return render_template("login.html")
