from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class UserForm(Form):
    username = StringField('Input your username', validators=[DataRequired()])
    password = PasswordField('Input your password', validators=[DataRequired()])
    submit = SubmitField('Submit')