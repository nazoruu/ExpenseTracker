from flask import Blueprint
from flask import Flask, redirect

view = Blueprint('view', __name__)

@view.route('/')
def default():
    return redirect('/login')

@view.route('/home')
def home():
    return "<p>Home</p>"