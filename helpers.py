import os

import requests
import urllib.parse
import flask
from functools import wraps


def login_required(f):
    @wraps(f)
    def decoratedFunc(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decoratedFunc
