from flask import render_template, url_for,redirect,flash
from main.forms import *
from main.models import *
from main import app

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

