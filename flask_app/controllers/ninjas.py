from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.ninja import Ninja # use the import path  from pagackage.folder.file <import whats in the file>
from flask_app.models.dojo import Dojo



# this route gets all ninjas by ID
@app.route("/dojo_info/<int:id>")
def get_ninjas(id):
    data = {"id": id}
    return render_template("show_dojo.html", dojo=Dojo.get_one(data))


# this rout gets all dojos
@app.route("/ninja_page")
def ninja_page():
    all_dojos = Dojo.get_all()
    return render_template("new_ninja.html", all_dojos=all_dojos)

# this route creates ninjas
@app.post("/create_ninja")
def create_ninja():
    dojo_id = request.form["dojo_id"]
    Ninja.save(request.form)
    return redirect(f"/dojo_info/{dojo_id}")


# this route edits ninjas
@app.get("/edit_ninja/<int:ninja_id>")
def edit_ninja(ninja_id):
    ninja = Ninja.find_by_id({"id": ninja_id})
    if ninja == None:
        return "Cannot find Ninja."
    return render_template("edit_ninja.html", ninja=ninja)

# this route updates ninjas
@app.post("/update_ninja")
def update_ninja():
    dojo_id = request.form["dojo_id"]
    Ninja.update(request.form)
    return redirect(f"/dojo_info/{dojo_id}")

# this reoute deletes ninjas
@app.post("/delete_ninja/<int:ninja_id>")
def delete_ninja(ninja_id):
    dojo_id = request.form["dojo_id"]
    Ninja.delete(ninja_id)
    return redirect(f"/dojo_info/{dojo_id}")


