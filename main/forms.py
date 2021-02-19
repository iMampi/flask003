from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length, Email, EqualTo

class RegistrationForm(FlaskForm):
	username = StringField('Username',
		validators=[DataRequired(),Length(min = 6, max=30)])
	email = StringField('Email',
		validators=[DataRequired(),Email()])
	password = PasswordField('Password',
		validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password',
		validators=[DataRequired(),EqualTo('password')])
	submit = SubmitField("SIGN UP")

class LoginForm(FlaskForm):
	email = StringField('Email',
		validators=[DataRequired(),Email(message="Not a valid email")])
	password = PasswordField('Password',
		validators=[DataRequired()])
	remember = BooleanField('Remember me')
	submit = SubmitField("LOG IN")