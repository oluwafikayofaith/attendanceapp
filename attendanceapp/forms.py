from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo 



class MyForm(FlaskForm):
    fullname = StringField("Fullame:",validators=[DataRequired(message='Field cannot be empty')]) 
    email = StringField("Email: ", validators=[Email(message='Please enter a valid email')])
    password = PasswordField("Password: ", validators=[DataRequired(message='Field cannot be empty'),Length(min=5,message='your password is too short')])
    phone = StringField("Phone Number:",validators=[DataRequired(message='Field cannot be empty')])
    matno = StringField("Matric no:",validators=[DataRequired(message='Field cannot be empty')])
    add = StringField("Address:",validators=[DataRequired(message='Address field cannot be empty')])
    confirm_password= PasswordField("Confirm Password: ",validators=[EqualTo('password')])
    submit = SubmitField("Register")

class LectureForm(FlaskForm):
    fullname = StringField("Fullame:",validators=[DataRequired(message='Field cannot be empty')]) 
    email = StringField("Email: ", validators=[Email(message='Please enter a valid email')])
    password = PasswordField("Password: ", validators=[DataRequired(message='Field cannot be empty'),Length(min=5,message='your password is too short')])
    phone = StringField("Phone Number:",validators=[DataRequired(message='Field cannot be empty')])
    add = StringField("Address:",validators=[DataRequired(message='Address field cannot be empty')])
    confirm_password= PasswordField("Confirm Password: ",validators=[EqualTo('password')])
    submit = SubmitField("Register")


class AdForm(FlaskForm):
    username = StringField("Username:",validators=[DataRequired(message='Field cannot be empty')])
    password = PasswordField("Password: ", validators=[DataRequired(message='Field cannot be empty'),Length(min=5,message='your password is too short')])
    submit = SubmitField("Register")


