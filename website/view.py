from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for, session
from flask_login import login_required, current_user
from .datamodel import User, Expense, Budget, Income, Category
from . import db
from datetime import datetime
import json
from .auth import auth

view = Blueprint('view', __name__)

@view.route('/')
def base():
    return redirect(url_for('auth.login'))

'''@view.route('/home')
def home():
    return render_template("home.html", user=current_user)'''

@view.route('/budget', methods=['GET', 'POST'])
def budget(): 
        user = Income.query.filter_by(user_id=session.get('user_id')).first()
        user_budget = Budget.query.filter_by(user_id=session.get('user_id')).first()
        if request.method == 'POST':
            income_str = request.form.get('income') 
            income = float(income_str)
            needs = income * 0.5
            wants = income * 0.3
            savings = income * 0.2
            user = Income.query.filter_by(user_id=session.get('user_id')).first()
            user_budget = Budget.query.filter_by(user_id=session.get('user_id')).first()
            if user:
                 user.amount = income
                 user_budget.budget_wants = wants
                 user_budget.budget_needs = needs
                 user_budget.budget_savings = savings
                 db.session.commit()
            else:
                 new_income = Income(amount = income, user_id = session.get('user_id'))
                 new_budget = Budget(budget_needs = needs, budget_wants = wants, budget_savings = savings, user_id = session.get('user_id'))
                 db.session.add(new_income)
                 db.session.add(new_budget)
                 db.session.commit()
        user = Income.query.filter_by(user_id=session.get('user_id')).first()
        user_budget = Budget.query.filter_by(user_id=session.get('user_id')).first()
        return render_template('budget.html', user=user, user_budget=user_budget)



@view.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Check if it's an expense form submission
        if 'amount' in request.form:
            amount = float(request.form.get('amount'))
            date = datetime.strptime(request.form.get('date'), '%Y-%m-%d')
            description = request.form.get('description')
            category_id = int(request.form.get('category'))

            # Fetch user's expense inside the POST request block
            user_expense = Expense.query.filter_by(user_id=session.get('user_id')).first()

            if user_expense:
                # Update existing expense
                user_expense.amount = amount
                user_expense.date = date
                user_expense.description = description
                user_expense.category_id = category_id
            else:
                # Create new expense object
                new_expense = Expense(amount=amount, date=date, description=description, category_id=category_id, user_id=session.get('user_id'))
                db.session.add(new_expense)

        # Check if it's a category form submission
        elif 'category_name' in request.form:
            category_name = request.form.get('category_name')
            user_categories = Category.query.filter_by(name=category_name, user_id=session.get('user_id')).first()

            if not user_categories:
                # Create new category object
                new_category = Category(name=category_name, user_id=session.get('user_id'))
                db.session.add(new_category)
                db.session.commit()

        db.session.commit()  # Commit changes after handling both forms
        return redirect('/home')  # Redirect to refresh the page

    # Fetch user data for display
    user_expense = Expense.query.filter_by(user_id=session.get('user_id')).first()
    user_categories = Category.query.filter_by(user_id=session.get('user_id')).all()

    return render_template("home.html", user=current_user, user_expense=user_expense, user_categories=user_categories)