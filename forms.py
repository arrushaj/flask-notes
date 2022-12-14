"""Forms for Notes app."""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, URL

class RegisterForm(FlaskForm):
    """Form for registering users."""

    username = StringField(
        "Username",
        validators=[InputRequired()])

    password = PasswordField(
        "Password",
        validators=[InputRequired()])

    email = StringField(
        "Email",
        validators=[InputRequired(), Email()])

    first_name = StringField(
        "First Name",
        validators=[InputRequired()])

    last_name = StringField(
        "Last Name",
        validators=[InputRequired()])

class LoginForm(FlaskForm):
    """Form to log in."""

    username = StringField(
        "Username",
        validators=[InputRequired()])

    password = PasswordField(
        "Password",
        validators=[InputRequired()])

class CSRFProtectForm(FlaskForm):
    """Form for CSRF protection."""

class AddNoteForm(FlaskForm):
    """Form for adding notes."""

    title = StringField(
        "Title",
        validators=[InputRequired()]
    )

    content = StringField(
        "Content",
        validators=[InputRequired()]
    )

class EditNoteForm(FlaskForm):
    """Form for editing notes."""

    title = StringField(
        "Title",
        validators=[InputRequired()]
    )

    content = StringField(
        "Content",
        validators=[InputRequired()]
    )