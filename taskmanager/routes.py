''' route files '''

from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    ''' home returns the tasks.html template as homepage '''
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    ''' returns the categories.html when categories is called '''
    return render_template("categories.html")


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    ''' returns the add_category.html when it is called '''
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")
