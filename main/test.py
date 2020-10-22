from flask import request
import unittest
import wikipedia
from main import app
from functions import *
from models import Racer
from db_helper import *


class BasicTests(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.app = app.test_client()
        init_db()

    def tearDown(self):
        reset_db()

    def test_db(self):
        for record in Racer.select():
            assert record.position
            assert record.name
            assert record.team
            assert record.time
            assert record.driver_id

    def test_db_get_record_about_driver(self):
        record1 = Racer.get(Racer.driver_id == "FAM")
        record2 = Racer.get(Racer.driver_id == "LHM")
        assert record1.team == "MCLAREN RENAULT"
        assert record1.name == "Fernando Alonso"
        assert record2.team == "MERCEDES"
        assert record2.name == "Lewis Hamilton"

    def test_wiki(self):
        record1 = Racer.get(Racer.driver_id == "FAM")
        record2 = Racer.get(Racer.driver_id == "LHM")
        assert wikipedia.page(record1.name).url
        assert wikipedia.page(record2.name).url

    def test_report(self):
        response = self.app.get("/report")
        self.assertEqual(response.status_code, 200)

    def test_report_asc(self):
        response = self.app.get("/report?order=asc")
        self.assertEqual(response.status_code, 200)

    def test_report_desc(self):
        response = self.app.get("/report?order=desc")
        self.assertEqual(response.status_code, 200)

    def test_drivers(self):
        response = self.app.get("/report/drivers")
        self.assertEqual(response.status_code, 200)

    def test_drivers_asc(self):
        response = self.app.get("/report/drivers?order=asc")
        self.assertEqual(response.status_code, 200)

    def test_drivers_desc(self):
        response = self.app.get("/report/drivers?order=desc")
        self.assertEqual(response.status_code, 200)

    def test_driver_id_middle_is_upper(self):
        response = self.app.get("/report/drivers?driver_id=fAm")
        self.assertEqual(response.status_code, 200)

    def test_driver_id_lower(self):
        response = self.app.get("/report/drivers?driver_id=fam")
        self.assertEqual(response.status_code, 200)

    def test_driver_id_upper(self):
        response = self.app.get("/report/drivers?driver_id=FAM")
        self.assertEqual(response.status_code, 200)

    def test_driver_id_args(self):
        with app.test_request_context('/report/drivers?driver_id=KRF'):
            assert request.path == '/report/drivers'
            assert request.args['driver_id'] == 'KRF'

    def test_report_request_args(self):
        with app.test_request_context('/report?order=asc'):
            assert request.path == '/report'
            assert request.args['order'] == 'asc'
        with app.test_request_context('/report?order=desc'):
            assert request.path == '/report'
            assert request.args['order'] == 'desc'

    def test_drivers_request_args(self):
        with app.test_request_context('/report/drivers?order=asc'):
            assert request.path == '/report/drivers'
            assert request.args['order'] == 'asc'
        with app.test_request_context('/report/drivers?order=desc'):
            assert request.path == '/report/drivers'
            assert request.args['order'] == 'desc'


if __name__ == '__main__':
    unittest.main()
