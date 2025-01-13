from flask import Blueprint, render_template
from peewee import *
from database.database import Professor

professor_route = Blueprint("professor", __name__)

db = SqliteDatabase([Professor])

@professor_route.route('/')
def list_professor():
     return render_template("list_professor.html")