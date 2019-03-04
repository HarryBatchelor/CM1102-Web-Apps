
from datetime import datetime
from shop import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20),nullable=False)
    last_name = db.Column(db.String(30),nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)

    def __repr__(self):
        return f"Author('{self.first_name}', '{self.last_name}')"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    description = db.Column(db.String(120), nullable=False)
    #publication_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    price = db.Column(db.Numeric(10,2), nullable=False)
    image_file = db.Column(db.String(30), nullable=False, default='default.jpg')
    stock_level = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def __repr__(self):
        return f"Book('{self.title}', '{self.description}', '{self.price}', '{self.stock_level}')"
