from flask_wtf import Form
from wtforms import TextAreaField,PasswordField,IntegerField,RadioField,SubmitField
#from cProfile import label
from wtforms.validators import ValidationError,DataRequired

class simpleform(Form):
    name = TextAreaField(label='Username', validators=[DataRequired()])
    Password = PasswordField(label='Password',validators=[DataRequired()])
    PhoneNumber = IntegerField(label='Mobile no.',validators=[DataRequired()])
    gender = RadioField(label='Gender', choices=['Male','Female'])
    address = TextAreaField(label='Address',)
    age = IntegerField(label='Age',)
    submit = SubmitField('Submit')