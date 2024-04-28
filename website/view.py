from flask import Blueprint, redirect, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .datamodel import User, Expense, Budget, Income, Category
from . import db
from datetime import datetime
import json

view = Blueprint('view', __name__)

@view.route('/')
def default():
    return redirect('/login')

@view.route('/home')
def home():
   return render_template("home.html", user=current_user)

'''@view.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get form data
        amount = float(request.form['amount'])
        date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        description = request.form['description']
        category_id = int(request.form['category'])

        # Create new expense object
        new_expense = Expense(amount=amount, date=date, description=description, category_id=category_id)
        
        # Add to database and commit
        db.session.add(new_expense)
        db.session.commit()

        return redirect('/home')   
    elif 'budget_amount' in request.form:  # Check if it's a budget form submission
        # Get form data
        budget_amount = float(request.form['budget_amount'])
        category_id = int(request.form['category'])

        # Create new budget object
        new_budget = Budget(budget_amount=budget_amount, category_id=category_id)
            
        # Add to database and commit
        db.session.add(new_budget)
        db.session.commit()

        return redirect('/home')

    elif 'category_name' in request.form:  # Check if it's a category form submission
        # Get category name from form data
        category_name = request.form['category_name']

        # Create new category object
        new_category = Category(name=category_name)
            
        # Add to database and commit
        db.session.add(new_category)
        db.session.commit()

        return redirect('/home')
    return render_template("home.html", user=current_user)'''