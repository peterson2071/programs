import os

import requests
import urllib.parse
from flask import Flask, redirect, render_template, flash, session, request
from functools import wraps


def login_required(f):
    @wraps(f)
    def decoratedFunc(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decoratedFunc
