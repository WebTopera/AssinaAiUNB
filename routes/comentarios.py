from flask import Blueprint, render_template

comentarios_route = Blueprint("comentarios", __name__)

@comentarios_route.route('/')
def home():
    return render_template("index.html")