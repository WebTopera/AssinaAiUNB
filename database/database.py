# from peewee import *

# db = SqliteDatabase("database.db")

# class Professor(Model):
#     name = CharField()
#     description = TextField()
#     image = CharField()
#     media = FloatField()
#     sum_grade = DecimalField()
#     q_avaliations = DecimalField()

#     class Meta:
#         database = db

# class Comentario(Model):
#     title = TextField()
#     description = TextField()
#     grade = DecimalField()
#     professor = ForeignKeyField(Professor, backref='comentarios')

#     class Meta:
#         database = db


PROFS = [
    {"id": 1, "name": "Leandro", "Description": "exemplo Descricao 1", "media": 0, "sum_grade": 0, "q_avaliations": 0, "filename": "leandro.png"},
    {"id": 2, "name": "Bruna", "Description": "exemplo Descricao 2", "media": 0, "sum_grade": 0, "q_avaliations": 0, "filename": "bruna.png"},
    {"id": 3, "name": "Carlos", "Description": "exemplo Descricao 3", "media": 0, "sum_grade": 0, "q_avaliations": 0, "filename": "carlos.png"},
    {"id": 4, "name": "Ana", "Description": "exemplo Descricao 4", "media": 0, "sum_grade": 0, "q_avaliations": 0, "filename": "ana.png"},
    {"id": 5, "name": "Pedro", "Description": "exemplo Descricao 5", "media": 0, "sum_grade": 0, "q_avaliations": 0, "filename": "pedro.png"},
    {"id": 6, "name": "Mariana", "Description": "exemplo Descricao 6", "media": 0, "sum_grade": 0, "q_avaliations": 0, "filename": "mariana.png"},
    {"id": 7, "name": "João", "Description": "exemplo Descricao 7", "media": 0, "sum_grade": 0, "q_avaliations": 0, "filename": "joao.png"},
    {"id": 8, "name": "Fernanda", "Description": "exemplo Descricao 8", "media": 0, "sum_grade": 0, "q_avaliations": 0, "filename": "fernanda.png"},
    {"id": 9, "name": "Lucas", "Description": "exemplo Descricao 9", "media": 0, "sum_grade": 0, "q_avaliations": 0, "filename": "lucas.png"},
    {"id": 10, "name": "Juliana", "Description": "exemplo Descricao 10", "media": 0, "sum_grade": 0, "q_avaliations": 0, "filename": "juliana.png"},
    {"id": 11, "name": "Ricardo", "Description": "exemplo Descricao 11", "media": 0, "sum_grade": 0, "q_avaliations": 0, "filename": "ricardo.png"},
    {"id": 12, "name": "Patrícia", "Description": "exemplo Descricao 12", "media": 0, "sum_grade": 0, "q_avaliations": 0, "filename": "patricia.png"}
]

COMETS = [
    {"id": 1,"title": "Comentário 1", "text": "Texto do comentário 1", "grade": 0, "professor_id": 1},
    {"id": 2,"title": "Comentário 2", "text": "Texto do comentário 2", "grade": 0, "professor_id": 2},
    {"id": 3,"title": "Comentário 3", "text": "Texto do comentário 3", "grade": 0, "professor_id": 3},
    {"id": 4,"title": "Comentário 4", "text": "Texto do comentário 4", "grade": 0, "professor_id": 4},
    {"id": 5,"title": "Comentário 5", "text": "Texto do comentário 5", "grade": 0, "professor_id": 5},
    {"id": 6,"title": "Comentário 6", "text": "Texto do comentário 6", "grade": 0, "professor_id": 6},
    {"id": 7,"title": "Comentário 7", "text": "Texto do comentário 7", "grade": 0, "professor_id": 7},
    {"id": 8,"title": "Comentário 8", "text": "Texto do comentário 8", "grade": 0, "professor_id": 8},
    {"id": 9,"title": "Comentário 9", "text": "Texto do comentário 9", "grade": 0, "professor_id": 9},
    {"id": 10,"title": "Comentário 10", "text": "Texto do comentário 10", "grade": 0, "professor_id": 10},
]