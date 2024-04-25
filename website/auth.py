from flask import Blueprint
from flask import render_template
from flask import redirect

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return redirect('/login')

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign-up</p>"