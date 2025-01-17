from flask import Blueprint, render_template, request, redirect, url_for
from database.database import COMETS, PROFS
from routes.professor import show_professor

comentarios_route = Blueprint("comentario", __name__)

@comentarios_route.route("/", methods=["POST"])
def insert_comentario(professor_id):
    id = len(COMETS) + 1
    title = request.form.get('title')
    texto = request.form.get('text')
    grade = request.form.get('grade', 0)
    professor_id = request.form.get('professor_id')
    if title and texto and professor_id:
        new_comentario = {
            "id": id,
            "title": title,
            "text": texto,
            "grade": grade,
            "professor_id": int(professor_id)
        }
        COMETS.append(new_comentario)
        return show_professor(int(professor_id))
    return redirect(url_for('comentario.list_comentarios'))

@comentarios_route.route("/new")
def form_comentario():
    return render_template("form_comentario.html", professores=PROFS)

@comentarios_route.route("/<int:comentario_id>")
def show_comentario(comentario_id):
    comentario = next((c for c in COMETS if c["id"] == comentario_id), None)
    if comentario:
        return render_template("show_comentario.html", comentario=comentario)
    return redirect(url_for('comentario.list_comentarios'))

@comentarios_route.route("/<int:comentario_id>/edit")
def edit_comentario(comentario_id):
    comentario = next((c for c in COMETS if c["id"] == comentario_id), None)
    if comentario:
        return render_template("form_comentario_edit.html", comentario=comentario, professores=PROFS)
    return redirect(url_for('comentario.list_comentarios'))

@comentarios_route.route("/<int:comentario_id>/update", methods=["POST"])
def update_comentario(comentario_id):
    comentario = next((c for c in COMETS if c["id"] == comentario_id), None)
    if comentario:
        comentario["title"] = request.form.get('title')
        comentario["text"] = request.form.get('texto')
        comentario["grade"] = request.form.get('grade', 0)
        comentario["professor_id"] = int(request.form.get('professor_id'))
        return redirect(url_for('comentario.show_comentario', comentario_id=comentario_id))
    return redirect(url_for('comentario.list_comentarios'))

@comentarios_route.route("/<int:comentario_id>/delete")
def delete_comentario(comentario_id):
    global COMETS
    COMETS = [c for c in COMETS if c["id"] != comentario_id]
    return redirect(url_for('comentario.list_comentarios'))