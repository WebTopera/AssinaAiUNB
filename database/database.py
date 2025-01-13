from peewee import *

db = SqliteDatabase("professores.db")

class Professores(Model):
    name = CharField()
    email = CharField()
    description = TextField()
    media = DecimalField()
    sum_notes = DecimalField()
    q_avaliations = DecimalField()

    class Meta:
        database = db

class Comentarios(Model):
    description = TextField()
    note = DecimalField()
    professor = ForeignKeyField()

    class Meta:
        database = db