import os
from flask import render_template, url_for, request, redirect, flash, session
from shop import app, db
from shop.models import Author, Book, User
from shop.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route("/home")
def home():
    books = Book.query.all()
    return render_template('home.html', books=books, title='My Wonderful Book Shop')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/book/<int:book_id>")
def book(book_id):
    book = Book.query.get_or_404(book_id)

    return render_template('book.html', book=book)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created.  You can now log in.')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            flash('You are now logged in.')
            return redirect(url_for('home'))
        flash('Invalid username or password.')

        return render_template('login.html', form=form)

    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

#Flask lab 3: implementation of Cart.  Needs 'session' import!
# https://github.com/kkschick/ubermelon-shopping-app/blob/master/melons.py MELONS

@app.route("/add_to_cart/<int:book_id>")
def add_to_cart(book_id):
    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(book_id)

    flash("The book is added to your shopping cart!")
    return redirect("/cart")


@app.route("/cart", methods=['GET', 'POST'])
def cart_display():
    if "cart" not in session:
        flash('There is nothing in your cart.')
        return render_template("cart.html", display_cart = {}, total = 0)
    else:
        items = session["cart"]
        cart = {}

        total_price = 0
        total_quantity = 0
        for item in items:
            book = Book.query.get_or_404(item)

            total_price += book.price
            if book.id in cart:
                cart[book.id]["quantity"] += 1
            else:
                cart[book.id] = {"quantity":1, "title": book.title, "price":book.price}
            total_quantity = sum(item['quantity'] for item in cart.values())


        return render_template("cart.html", title='Your Shopping Cart', display_cart = cart, total = total_price, total_quantity = total_quantity)

    return render_template('cart.html')

@app.route("/delete_book/<int:book_id>", methods=['GET', 'POST'])
def delete_book(book_id):
    if "cart" not in session:
        session["cart"] = []

    session["cart"].remove(book_id)

    flash("The book has been removed from your shopping cart!")

    session.modified = True

    return redirect("/cart")
