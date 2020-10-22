from playhouse.shortcuts import model_to_dict
from functions import *
from models import *
from db_helper import *


full_report = []
for record in Racer.select():
    full_report.append(model_to_dict(record))


def full_report_for_api(order="asc"):
    try:
        if order.lower() == "desc":
            return list(reversed(full_report))
        return full_report
    except Exception as err:
        print(err)
        return "Data files are broken.", 404


def make_the_drivers_report_for_api(order="asc"):
    try:
        if order.lower() == "desc":
            rev = True
        else:
            rev = False
        drivers_report = list(sorted(full_report, reverse=rev, key=lambda x: x["name"]))
        return drivers_report
    except Exception as err:
        print(err)
        return "There is an error in the data files.", 404


def get_record_about_driver_for_api(driver_id):
    try:
        driver = Racer.select().where(Racer.driver_id == driver_id.upper())
        driver = driver[0]
        return model_to_dict(driver)
    except Exception as err:
        print(err)
        return "There is not a driver with that code.", 404
