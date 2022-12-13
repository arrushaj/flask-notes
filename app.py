"""Notes application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User
from forms import RegisterForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///notes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)

@app.get("/")
def redirect_register():
    """Redirect to /register"""

    return redirect("/register")

@app.route("/register", methods=["GET", "POST"])
def register_user():
    """Show form to register users"""

    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        user = User.register(username, password, email, first_name, last_name)

        db.session.add(user)
        db.session.commit()

        return redirect('/home')

    else:
        return render_template("register.html", form=form)


