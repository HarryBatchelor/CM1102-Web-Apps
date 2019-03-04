from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'XXXXXXXXXX.........'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://YOUR_USERNAME:YOUR_MYSQL_PASSWORD@csmysql.cs.cf.ac.uk:3306/YOUR_DATABASE'
#e.g.c1234567:mypassword@csmysql.cs.cf.ac.uk:3306/c1234567

db = SQLAlchemy(app)

from shop import routes
