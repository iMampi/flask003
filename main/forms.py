from main.models import User
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length, Email, EqualTo,ValidationError


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

	def validate_username(self,field):
		user=User.query.filter_by(username=field.data).first()
		if user:
			raise ValidationError('This username is already used. Please, choose another.')
			
	def validate_email(self,field):
		email=User.query.filter_by(email=field.data).first()
		if email:
			raise ValidationError('This email is already used. Please, use another one.')

class LoginForm(FlaskForm):
	email = StringField('Email',
		validators=[DataRequired(),Email(message="Not a valid email")])
	password = PasswordField('Password',
		validators=[DataRequired()])
	remember = BooleanField('Remember me')
	submit = SubmitField("LOG IN")