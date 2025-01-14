from flask import Blueprint, render_template

comentarios_route = Blueprint("comentarios", __name__)

@comentarios_route.route("/")
def list_comentario():
     return render_template("list_comentario.html")

@comentarios_route.route("/", methods=["POST"])
def insert_comentario():
     return render_template("item_comentario.html")

@comentarios_route.route("/new")
def form_comentario():
     return render_template("form_comentario.html")

@comentarios_route.route("/<int:comentario_id>")
def show_comentario(comentario_id):
     return render_template("show_comentario.html")

@comentarios_route.route("/<int:comentario_id>/edit")
def edit_comentario(comentario_id):
     return render_template("form_comentario.html")

@comentarios_route.route("/<int:comentario_id>/update")
def update_comentario(comentario_id):
     return render_template("item_comentario.html")

@comentarios_route.route("/<int:comentario_id>/delete")
def delete_comentario(comentario_id):
     return {"deleted": "ok"}