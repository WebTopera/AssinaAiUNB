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


PROFS = [{"id":1,"name": "Leandro", "filename":"Topera.jpg"},{"id":2,"name": "Bruna", "filename":"Topera1.jpg"},{"id":3,"name": "BOLSOLULA", "filename":"Topera2.jpg"}]

