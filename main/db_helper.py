from peewee import *
from collections import OrderedDict
from functions import *
from models import *


def init_db(data=build_dict_for_database()):
    Racer.create_table()
    count_of_invalid_keys = 0
    pos = 1
    data = OrderedDict(sorted(data.items(), key=lambda x: x[1]['time']))
    for abb in data:
        if data[abb]["time"] == timedelta(0):
            count_of_invalid_keys += 1

    for abb in list(data.keys())[:-count_of_invalid_keys]:
        if data[abb]["time"] == timedelta(0):
            data.move_to_end(abb)
    for abb in data:
        db_dict = dict()
        time = data[abb]["time"]
        db_dict["name"], db_dict["team"] = data[abb]["name"], data[abb]["team"]
        if time == timedelta(0):
            db_dict["position"] = "*** ERROR"
            db_dict["time"] = "----- INVALID DATA! -----"
        else:
            db_dict["position"] = pos
            db_dict["time"] = str(time)[3:-3]
        pos += 1
        db_dict["driver_id"] = abb
        if not Racer.select().where(Racer.driver_id == db_dict["driver_id"]):
            Racer.create(**db_dict)


def reset_db():
    Racer.delete().execute()
