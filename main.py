from flask import Flask, redirect, request
from peewee import SqliteDatabase
from routes.home import home_route
from routes.comentarios import comentarios_route
from routes.professor import professor_route
# from database.database import Comentario, Professor

app = Flask(__name__)

#db = SqliteDatabase([Comentarios, Professores])

app.register_blueprint(home_route)
app.register_blueprint(comentarios_route, url_prefix="/comentarios")
app.register_blueprint(professor_route, url_prefix="/professores")

app.run(debug=True, port=5000)