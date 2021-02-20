from flask import render_template, url_for,redirect,flash,request
from flask_login.utils import logout_user
from main.forms import *
from main.models import *
from main import app, bcrypt, db
from flask_login import login_user,current_user,login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username =form.username.data, email = form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for{form.username.data}! You can try to log in.','success')
        return redirect(url_for('login'))
    return render_template("register.html",title="Register",form=form)

@app.route("/login/", methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')
            flash('Welcome back!','success')

            if next_page:
                return redirect(next_page)
            else:
                #flash(f'Welcome {current_user.username}!','success')
                return redirect(url_for('home'))
        else:
            flash('You are not registered! Sign up','danger')
            return redirect(url_for('register'))
    return render_template("login.html",title="Log In",form=form)

@app.route("/logout/")
def logout():
    logout_user()
    flash('Successfully logout. See you!','success')
    return redirect(url_for('home'))

@app.route("/profil/",methods=["GET","POST"])
@login_required
def profil():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username=form.username.data
        current_user.email=form.email.data
        db.session.commit()
        flash ('Your account has been updated','success')
        return redirect(url_for('profil'))
    elif request.method=='GET':
        form.username.data= current_user.username
        form.email.data=current_user.email
    image_file = url_for('static',
        filename='avatars/'+current_user.avatar_file)
    return render_template("profil.html",
        title="Profil",avatar=image_file,form=form)
   

