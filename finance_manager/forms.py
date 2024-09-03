from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class userLogin(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=24)], name="loginUsername")
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)], name="loginPassword")
    loginBtn = SubmitField("Login")

class userCreate(FlaskForm):
    createUsername = StringField("Username", validators=[DataRequired(), Length(min=2, max=24)], name="createUsername")
    createPassword = PasswordField("Enter Password", validators=[DataRequired(), Length(min=8)], name="createPassword")
    confirmPassword = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('createPassword')])
    createBtn = SubmitField("Create Account")

