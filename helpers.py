import os

import requests
import urllib.parse
import flask
from functolls import wraps

def apology(message, code=400):
    for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message))


def login_required(f):
    @wraps(f)
    def decoratedFunc(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decoratedFunc
