"""Models for Notes."""

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()
db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    app.app_context().push()
    db.app = app
    db.init_app(app)


class User(db.Model):
    __tablename__ = "users"

    @classmethod
    def register(cls, username, pwd, email, first_name, last_name):
        """Register user w/hashed password & return user."""

        hashed = bcrypt.generate_password_hash(pwd).decode('utf8')

        # return instance of user w/username and hashed pwd
        return cls(username=username, password=hashed, email=email,
                first_name=first_name, last_name=last_name)


    username = db.Column(
        db.String(20),
        primary_key=True,
    )

    password = db.Column(
        db.String(100),
        nullable=False)

    email = db.Column(
        db.String(50),
        nullable=False,
        unique=True)

    first_name = db.Column(
        db.String(30),
        nullable=False)

    last_name = db.Column(
        db.String(30),
        nullable=False)

