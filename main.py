import datetime as dt
from flask import Flask, render_template, url_for,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from flask.templating import render_template_string
from sqlalchemy.orm import backref
from forms import RegistrationForm,LoginForm

app=Flask(__name__)


#i used secrets.token_hex(16) to create a random secret_key
app.config['SECRET_KEY'] = '1bc511ffb35deac56b1cf85b5e09f083'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db=SQLAlchemy(app)

posts=[{
    "date":"14/02/2021",
    "author":"iMampi",
    "post":"C'est la St-Valentin.",
    "title":"<3"
    },
    {"date":"18/02/2021",
    "author":"iMampi",
    "post":"j'ai cru mourrir.",
    "title":"ill"

    }
]

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    avatar_file = db.Column(db.String(20),nullable=False,default="default.jpg")
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship('Post',backref='author',lazy=True)

    def __repr__():
        return f"User('{self.username}','{self.email}','{self.avatar_file}')"

class Post(db.Model):
    __tablename__='post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120),nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=dt.datetime.utcnow)
    post = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    def __repr__():
        return f"User('{self.title}','{self.date_posted}')"

@app.route("/")
@app.route("/home/")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about/")
def about():
    return render_template("about.html",title="About")

@app.route("/register/", methods=["GET","POST"])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for{form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template("register.html",title="Register",form=form)

@app.route("/login/", methods=["GET","POST"])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data =='admin@gmail.com' and form.password.data == '000':
            flash(f'Welcome Admin!','success')
            return redirect(url_for('home'))
        else:
             flash('You are not registered! Sign up','danger')
    return render_template("login.html",title="Log In",form=form)

if __name__=='__main__':
    app.run(debug=True)