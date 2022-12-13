"""Forms for Notes app."""
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, Email, URL

class RegisterForm(FlaskForm):
    """Form for registering users"""

    username = StringField("Username", validators=[InputRequired()])

    password = StringField("Password", validators=[InputRequired()])

    email = StringField("Email", validators=[InputRequired(), Email()])

    first_name = StringField("First Name", validators=[InputRequired()])

    last_name = StringField("Last Name", validators=[InputRequired()])