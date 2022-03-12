''' route files '''

from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    ''' home returns the base.html template '''
    return render_template("base.html")
