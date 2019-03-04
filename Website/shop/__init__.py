from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b27b2a1959efe4c2ac3991ce8350c16fd87da71d91dcfa92'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://C1816377:Hbatchelor8@csmysql.cs.cf.ac.uk:3306/C1816377'

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)

from shop import routes
