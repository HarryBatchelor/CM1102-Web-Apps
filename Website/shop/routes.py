import os
from flask import render_template, url_for, request, redirect, flash
from shop import app, db
from shop.models import Maker, Item, User
from shop.form import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route("/home")
def home():
    items = Item.query.all()
    return render_template('home.html', items=items, title='My Shop')

@app.route("/account")
def account():
    return render_template('account.html', title='Account')

@app.route("/checkout")
def checkout():
    return render_template('checkout.html', title='Checkout')

@app.route("/item/<int:item_id>")
def item(item_id):
    item = Item.query.get_or_404(item_id)
    return render_template('item.html', title=item.title, item=item)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
