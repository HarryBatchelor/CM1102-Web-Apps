import os
from flask import render_template, url_for, request, redirect, flash, session
from shop import app, db
from shop.models import Maker, Item, User
from shop.form import RegistrationForm, LoginForm, SearchForm
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = SearchForm()
    search = SearchForm(request.form)
    search_string = ""
    if request.method == 'POST':
        search_string = search.data['search']
        items = Item.query.filter(Item.item_name == search_string)
        return render_template('home.html', items=items, form=form)
    else:
        items = Item.query.all()
        return render_template('home.html', items=items, form=form)

@app.route("/HightoLow", methods=['GET', 'POST'])
def High_to_Low():
    form = SearchForm()
    search = SearchForm(request.form)
    items = Item.query.order_by(Item.price)
    items = items[::-1]
    search_string = ""
    if request.method == 'POST':
        search_string = search.data['search']
        items = Item.query.filter(Item.item_name == search_string)
        return render_template('home.html', items=items, form=form)
    else:
        items = Item.query.all()
        return render_template('home.html', items=items, form=form)

@app.route("/finished")
def finished():
    session["cart"].clear()
    session["wishlist"].clear()
    return render_template('finished.html', title='Thank you')

@app.route("/checkout")
def checkout():
    return render_template('checkout.html', title='Checkout')

@app.route("/item/<int:item_id>")
def item(item_id):
    item = Item.query.get_or_404(item_id)
    return render_template('item.html', title=item.item_name, item=item)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
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
    session['cart'].clear()
    logout_user()
    return redirect(url_for('home'))

@app.route("/add_to_cart/<int:item_id>")
def add_to_cart(item_id):
    if "cart" not in session:
        session["cart"] = []
    session["cart"].append(item_id)
    flash("The item has been added to your basket")
    return redirect("/cart")

@app.route("/cart", methods=['GET', 'POST'])
def cart_display():
    if "cart" not in session:
        flash('There is nothing in your basket.')
        return render_template("cart.html", display_cart = {}, total = 0)
    else:
        products = session["cart"]
        cart = {}

        total_price = 0
        total_quantity = 0
        for product in products:
            item = Item.query.get_or_404(product)

            total_price += item.price
            if item.id in cart:
                cart[item.id]["quantity"] += 1
            else:
                cart[item.id] = {"quantity":1, "Product name": item.item_name, "price":item.price}
            total_quantity = sum(product['quantity'] for product in cart.values())

        return render_template("cart.html", title= "Your basket", display_cart = cart, total = total_price, total_quantity = total_quantity)

    return render_template('cart.html')

@app.route("/add_to_wishlist/<int:item_id>")
def add_to_wishlist(item_id):
    if "wishlist" not in session:
        session["wishlist"] = []
    session["wishlist"].append(item_id)
    flash("The item has been added to your wishlist")
    return redirect("/wishlist")

@app.route("/wishlist", methods=['GET', 'POST'])
def wishlist_display():
    if "wishlist" not in session:
        flash('There is nothing in your wishlist.')
        return render_template("wishlist.html", display_wishlist = {}, total = 0)
    else:
        products = session["wishlist"]
        wishlist = {}

        total_price = 0
        total_quantity = 0
        for product in products:
            item = Item.query.get_or_404(product)

            total_price += item.price
            if item.id in wishlist:
                wishlist[item.id]["quantity"] += 1
            else:
                wishlist[item.id] = {"quantity":1, "Product name": item.item_name, "price":item.price}
            total_quantity = sum(product['quantity'] for product in wishlist.values())

        return render_template("wishlist.html", title= "Your basket", display_wishlist = wishlist, total = total_price, total_quantity = total_quantity)

@app.route("/delete_item/<int:item_id>", methods=['GET', 'POST'])
def delete_item(item_id):
    if "cart" not in session:
        session["cart"] = []
    session["cart"].remove(item_id)

    flash("The item has been removed from your basket")
    session.modified = True
    return redirect("/cart")

@app.route("/delete_item_wishlist/<int:item_id>", methods=['GET', 'POST'])
def delete_item_wishlist(item_id):
    if "wishlist" not in session:
        session["wishlist"] = []
    session["wishlist"].remove(item_id)

    flash("The item has been removed from your wishlist")
    session.modified = True
    return redirect("/wishlist")
