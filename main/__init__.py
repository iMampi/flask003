from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

#i used secrets.token_hex(16) to create a random secret_key
app.config['SECRET_KEY'] = '1bc511ffb35deac56b1cf85b5e09f083'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db=SQLAlchemy(app)

from main import routes