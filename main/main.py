from flask import render_template, request, redirect
import connexion
import wikipedia
from functions import *
from db_helper import *


init_db()

app = connexion.App(__name__, specification_dir="./")
app.add_api('swagger.yaml')


def get_order():
    if "order" in request.args:
        return request.args['order']
    return "asc"



@app.route("/")
def server():
    return redirect("http://localhost:5000/report")


@app.route("/report")
def full_report():
    order = get_order()
    db = Racer.select().order_by(-Racer.id) if order == "desc" else Racer.select()
    return render_template("report.html",
                           db=db)


@app.route("/report/drivers", methods=["GET", "POST"])
def show_driver():
    driver_id = ""
    if request.method == "POST":
        driver_id = request.form["driver_id"].upper()
    elif "driver_id" in request.args:
        driver_id = request.args["driver_id"]
    else:
        order = get_order()
        key = -Racer.name if order == "desc" else Racer.name
        db = Racer.select().order_by(key)
        return render_template("drivers.html", db=db)

    rec = Racer.select().where(Racer.driver_id == driver_id.upper())
    record = rec[0]
    wiki_info = wikipedia.summary(record.name, sentences=3)
    wiki_url = wikipedia.page(record.name).url
    return render_template("driver_id.html", record=record,
                           wiki_info=wiki_info,
                           wiki_url=wiki_url)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    reset_db()