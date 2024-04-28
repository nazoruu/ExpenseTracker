from flask import Blueprint
from flask import Flask, redirect, render_template

view = Blueprint('view', __name__)

@view.route('/')
def default():
    return redirect('/login')

@view.route('/home')
def home():
    return "<p>Home</p>"

@view.route('/budget')
def budget():
    return render_template("budget.html")