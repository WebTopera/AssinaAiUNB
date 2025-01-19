from flask import Blueprint, render_template, request, redirect, url_for
from database.database import COMETS, PROFS
from routes.professor import show_professor

comentarios_route = Blueprint("comentario", __name__)

@comentarios_route.route("/", methods=["POST"])
def insert_comentario():
    id = len(COMETS) + 1
    title = request.form.get('title')
    texto = request.form.get('text')    
    professor_id = request.form.get('id_professor')
    if title and texto and professor_id:
        new_comentario = {
            "id": id,
            "title": title,
            "text": texto,
            "professor_id": int(professor_id)
        }
        COMETS.append(new_comentario)
        return show_professor(int(professor_id))
    return redirect(url_for('comentario.list_comentarios'))

@comentarios_route.route("/new_comentario")
def form_comentario():
    return render_template("form_comentario.html", professores=PROFS)
