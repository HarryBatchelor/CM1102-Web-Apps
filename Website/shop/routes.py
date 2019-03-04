import os
from flask import render_template, url_for, request
from shop import app
from shop.models import Author, Book

@app.route("/")
@app.route("/home")
def home():
    books = Book.query.all()
    return render_template('home.html', books=books)

@app.route("/account")
def about():
    return render_template('account.html', title='Account')
