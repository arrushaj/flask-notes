"""Notes application."""

from flask import Flask, request, redirect, render_template, session, flash
from models import db, connect_db, User, Note
from forms import RegisterForm, LoginForm, CSRFProtectForm, AddNoteForm

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

        session["user_id"] = user.username

        return redirect(f'/users/{user.username}')

    else:
        return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login_user():
    """Shows login form if not logged in, otherwise redirect to secret page."""

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)

        if user:
            session["user_id"] = user.username
            return redirect(f"/users/{user.username}")
        else:
            form.username.errors = ["Bad username/password"]

    return render_template("login.html", form=form)

@app.get("/users/<username>")
def show_user(username):
    """Shows logged in user's profile."""

    form = CSRFProtectForm()

    if "user_id" not in session:
        flash("You must be logged in to view!")

        return redirect("/")

    else:
        user = User.query.get_or_404(username)

        notes = user.notes

        return render_template("user.html", user=user, form=form, notes=notes)

@app.post("/logout")
def logout_user():
    """Logs out the user."""

    form = CSRFProtectForm()

    if form.validate_on_submit():
        session.pop("user_id", None)

        return redirect("/")

@app.post("/users/<username>/delete")
def delete_user(username):
    """Delete the user"""

    form = CSRFProtectForm()

    if form.validate_on_submit():
        user = User.query.get_or_404(username)
        notes = user.notes

        for note in notes:
            db.session.delete(note)

        db.session.commit()

        db.session.delete(user)
        db.session.commit()

        session.pop("user_id", None)

        return redirect('/')

@app.route("/users/<username>/notes/add", methods=["GET", "POST"])
def add_note(username):
    """Add note"""

    form = AddNoteForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        note = Note(title=title, content=content, owner=username)

        db.session.add(note)
        db.session.commit()

        return redirect(f'/users/{username}')

    else:
        return render_template("note.html", form=form)