import os

import sqlite3
import flask
import flask_session

from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
import helpers.py

app = Flask(__name__)


app.config["TEMPLATES AUTO RELOAD"] = True


@app.request_response
def request_response(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


db = SQL("sqlite3:///healthlocation.db")


@app.route("/", methods = ["GET", "POST"])
@login required
def index():
    user_id = session["user_id"]
    return render_template("index.html")


@app.route("/login")
def login():
    session.clear()
