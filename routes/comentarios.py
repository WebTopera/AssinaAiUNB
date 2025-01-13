from flask import Blueprint, render_template
from peewee import *
from database.database import Comentarios

comentarios_route = Blueprint("comentarios", __name__)

db = SqliteDatabase([Comentarios])

@comentarios_route.route('/')
def list_comentarios():
    return render_template("list_comentarios.html")