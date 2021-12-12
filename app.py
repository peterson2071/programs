import os

import sqlite3
import flask
from flask_session import Session

from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required

app = flask.Flask(__name__)


app.config["TEMPLATES AUTO RELOAD"] = True


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


db = sqlite3.connect("healthlocation.db")


@app.route("/")
@login_required
def index():
    user_id = session["user_id"]
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username:
            return render_template("apology.html", message="Missing username")
        if not password:
            return render_template("apology.html", message="Missing password")
        rows = db.execute("SELECT * FROM users WHERE username=?", username)
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return render_template("apology.html", message="Invalid username and/or password")
        session["user_id"] = rows[0]["id"]
        return redirect("/")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        passwordConfirm = request.form.get("passwordConfirm")
        if not username:
            return render_template("apology.html", message="Missing username")
        if not password:
            return render_template("apology.html", message="Missing password")
        if not passwordConfirm:
            return render_template("apology.html", message="Repeat your password")
        if password != passwordConfirm:
            return render_template("apology.html", message="Two different passwords")
        if len(password) < 8 or len(password) > 20:
            return render_template("apology.html", message="Too short/long password")
        hash = generate_password_hash(password)
        common_username = db.execute("SELECT username FROM users WHERE username=?", username)
        if common_username:
            return render_template("apology.html", message="Already existent username")
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash)
        return redirect("/")
    else:
        return render_template("register.html")
