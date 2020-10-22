from peewee import *

db = SqliteDatabase("report.db")


class Racer(Model):
    position = IntegerField()
    name = CharField()
    team = CharField()
    time = CharField()
    driver_id = CharField()

    class Meta:
        database = db
