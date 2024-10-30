from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask import render_template, request, redirect

# use the import path  from pagackage.folder.file <import whats in the file>
# import the ninja.py from controllers


# ==========================================
# This is the begining route from the index
# ==========================================
@app.route("/")
def index():
    """This route displays all dojos"""
    return redirect("/dojos")  # this redirects to dojos


@app.route("/dojos")
def dashboard():
    """This shows all the dojos"""
    return render_template("dojos.html", all_dojos=Dojo.get_all()) # this takes the information from the


@app.post("/create_dojo")
def create_dojo():
    """ This creates a dojo"""
    data = {"name": request.form["name"]}
    Dojo.save(data)
    return redirect("/")  # this sends it back to the list of dojos


