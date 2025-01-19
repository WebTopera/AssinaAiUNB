from flask import Blueprint, render_template, request, redirect, url_for
from database.database import PROFS, COMETS
import os

professor_route = Blueprint("professor", __name__)

@professor_route.route("/")
def list_professor():
    return render_template("list_professor.html", professores=PROFS)

@professor_route.route("/", methods=["POST"])
def insert_professor():
    id = PROFS[-1]["id"] + 1
    nome = request.form.get('nome')
    descricao = request.form.get('description')
    arquivo = request.files.get('perfil-professor')
    if arquivo and nome and descricao:
        filepath = os.path.join("static", "images", arquivo.filename)

        arquivo.save(filepath)

        new_professor = {
            "id": id,
            "name": nome,
            "Description": descricao,
            "media": 0,
            "sum_grade": 0,
            "q_avaliations": 0,
            "filename": arquivo.filename
        }
        PROFS.append(new_professor)
        return redirect(url_for('home.home'))
    return redirect(url_for('professor.list_professor'))

@professor_route.route("/new")
def form_professor():
    return render_template("form_professor.html")

@professor_route.route("/<int:professor_id>")
def show_professor(professor_id):
    professor = next((p for p in PROFS if p["id"] == professor_id), None)
    comentarios = [c for c in COMETS if c["professor_id"] == professor_id]
    if professor:
        return render_template("show_professor.html", professor=professor, comentarios=comentarios)
    return redirect(url_for('professor.list_professor'))

@professor_route.route("/<int:professor_id>/edit")
def edit_professor(professor_id):
    professor = next((p for p in PROFS if p["id"] == professor_id), None)
    if professor:
        return render_template("form_professor_edit.html", professor=professor)
    return redirect(url_for('professor.list_professor'))

@professor_route.route("/<int:professor_id>/update", methods=["POST"])
def update_professor(professor_id):
    professor = next((p for p in PROFS if p["id"] == professor_id), None)
    if professor:
        professor["name"] = request.form.get('name')
        professor["Description"] = request.form.get('description')
        professor["filename"] = request.files.get('perfil-professor').filename
        return redirect(url_for('professor.show_professor', professor_id=professor_id))
    return redirect(url_for('professor.list_professor'))

@professor_route.route("/<int:professor_id>/delete")
def delete_professor(professor_id):
    global PROFS
    PROFS = [p for p in PROFS if p["id"] != professor_id]
    return redirect(url_for('professor.list_professor'))