from flask_login import UserMixin
from main import db,login_manager
import datetime as dt

#must be created. we tell login manager how to get user from our db
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
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
