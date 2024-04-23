from flask import Blueprint

view = Blueprint('view', __name__)

@view.route('/')
def home():
    return "<h1>Test</h1>"