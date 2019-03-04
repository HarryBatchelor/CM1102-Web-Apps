import os
from flask import render_template, url_for, request
from shop import app
from shop.models import Maker, Item

@app.route("/")
@app.route("/home")
def home():
    item = Item.query.all()
    return render_template('home.html', item=item)

@app.route("/account")
def account():
    return render_template('account.html', title='Account')
