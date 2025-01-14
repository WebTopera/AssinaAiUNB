from flask import Blueprint, render_template

professor_route = Blueprint("professor", __name__)

@professor_route.route("/")
def list_professor():
     return render_template("list_professor.html")

@professor_route.route("/", methods=["POST"])
def insert_professor():
     return render_template("item_professor.html")

@professor_route.route("/new")
def form_professor():
     return render_template("form_professor.html")

@professor_route.route("/<int:professor_id>")
def show_professor(professor_id):
     return render_template("show_professor.html")

@professor_route.route("/<int:professor_id>/edit")
def edit_professor(professor_id):
     return render_template("form_professor_edit.html")

@professor_route.route("/<int:professor_id>/update")
def update_professor(professor_id):
     return render_template("item_professor.html")

@professor_route.route("/<int:professor_id>/delete")
def delete_professor(professor_id):
     return {"deleted": "ok"}