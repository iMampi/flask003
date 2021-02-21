from main.models import User
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length, Email, EqualTo,ValidationError
from flask_login import current_user

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

class UpdateAccountForm(FlaskForm):
	username = StringField('Username',
		validators=[DataRequired(),Length(min = 6, max=30)])
	email = StringField('Email',
		validators=[DataRequired(),Email()])
	picture =FileField('Update avatar', validators=[FileAllowed(['jpg','jpeg','png'])])
	submit = SubmitField("Save updates")

	def validate_username(self,field):
		if field.data != current_user.username:
			user=User.query.filter_by(username=field.data).first()
			if user:
				raise ValidationError('This username is already used. Please, choose another.')
			
	def validate_email(self,field):
		if field.data != current_user.email:
			email=User.query.filter_by(email=field.data).first()
			if email:
				raise ValidationError('This email is already used. Please, use another one.')

class PostForm(FlaskForm):
	title = StringField('Title',validators=[DataRequired()])
	content = TextAreaField('Content',validators=[DataRequired()])
	submit = SubmitField("Post")
