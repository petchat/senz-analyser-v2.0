from unittest import TestCase
from flask_app.app import app
import json

class TestMiddlewarePoi2PoiProb(TestCase):

    def setUp(self):
        super(TestMiddlewarePoi2PoiProb, self).setUp()
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        super(TestMiddlewarePoi2PoiProb, self).tearDown()
        app.config['TESTING'] = False

    def testPredictPoi(self):
        input = {

        }
        rv = self.app.post("/classifyGMMHMM/", data=json.dumps(input))
        self.assertEqual(200, rv.status_code)
        result = json.loads(rv.data)
        self.assertEqual(0, result['code'])

    def testTrainPoi(self):
        input = {

        }
        rv = self.app.post("/trainingGMMHMM/", data=json.dumps(input))
        self.assertEqual(200, rv.status_code)
        result = json.loads(rv.data)
        self.assertEqual(0, result['code'])