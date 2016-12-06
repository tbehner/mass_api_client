import json
import unittest

import requests
from httmock import urlmatch, HTTMock

from mass_api_client import MASSApi
from mass_api_client.schemas.report import ReportSchema
from mass_api_client.schemas.scheduled_analysis import ScheduledAnalysisSchema


class MASSApiTestCase(unittest.TestCase):
    def setUp(self):
        self.api_key = '1234567890abcdef'
        self.base_url = 'http://localhost/api/'
        self.example_data = {'lorem': 'ipsum', 'integer': 1}

    def test_getting_json(self):
        @urlmatch(netloc=r'localhost', path=r'/api/json')
        def mass_mock_get_json(url, request):
            self.assertEqual(request.headers['Authorization'], 'APIKEY {}'.format(self.api_key))
            return json.dumps(self.example_data)

        with HTTMock(mass_mock_get_json):
            ma = MASSApi(api_key=self.api_key, base_url=self.base_url)
            response = ma._get_json('http://localhost/api/json')

        self.assertEqual(self.example_data, response)

    def test_posting_json(self):
        @urlmatch(netloc=r'localhost', path=r'/api/json')
        def mass_mock_post_json(url, request):
            self.assertEqual(request.headers['Authorization'], 'APIKEY {}'.format(self.api_key))
            self.assertEqual(json.loads(request.body), self.example_data)
            return json.dumps(self.example_data)

        with HTTMock(mass_mock_post_json):
            ma = MASSApi(api_key=self.api_key, base_url=self.base_url)
            response = ma._post_json('http://localhost/api/json', data=self.example_data)

        self.assertEqual(self.example_data, response.json())

    def test_receiving_server_error(self):
        @urlmatch(netloc=r'localhost', path=r'/api/json')
        def mass_mock_forbidden(url, request):
            return {'status_code': 403,
                    'content': json.dumps('{"error": "Access denied"}')}

        with HTTMock(mass_mock_forbidden):
            ma = MASSApi(api_key=self.api_key, base_url=self.base_url)
            self.assertRaises(requests.exceptions.HTTPError, lambda: ma._get_json('http://localhost/api/json'))
            self.assertRaises(requests.exceptions.HTTPError, lambda: ma._post_json('http://localhost/api/json', self.example_data))

    def test_getting_scheduled_analyses(self):
        with open('tests/data/scheduled_analyses.json') as data_file:
            data = json.load(data_file)

        @urlmatch(netloc=r'localhost',
                  path=r'/api/analysis_system_instance/b200ad66-f18a-4b37-b251-91d5ee948ef4/scheduled_analyses/')
        def mass_mock_get_scheduled_analyses(url, request):
            self.assertEqual(request.headers['Authorization'], 'APIKEY {}'.format(self.api_key))
            return json.dumps(data)

        with HTTMock(mass_mock_get_scheduled_analyses):
            ma = MASSApi(api_key=self.api_key, base_url=self.base_url)
            analyses = ma.get_scheduled_analyses('b200ad66-f18a-4b37-b251-91d5ee948ef4')

        serialized = ScheduledAnalysisSchema(many=True).dump(analyses)
        self.maxDiff = None
        self.assertEqual(data['results'], serialized.data)

    def test_getting_report(self):
        with open('tests/data/report.json') as data_file:
            data = json.load(data_file)

        @urlmatch(netloc=r'localhost',
                  path=r'/api/report/58362185a7a7f10843133337/')
        def mass_mock_get_report(url, request):
            self.assertEqual(request.headers['Authorization'], 'APIKEY {}'.format(self.api_key))
            return json.dumps(data)

        with HTTMock(mass_mock_get_report):
            ma = MASSApi(api_key=self.api_key, base_url=self.base_url)
            report = ma.get_report('58362185a7a7f10843133337')

        serialized, errors = ReportSchema().dump(report)
        self.assertEqual(data, serialized)

    def test_invalid_data_deserialization(self):
        data = {"test": "invalid"}

        @urlmatch(netloc=r'localhost',
                  path=r'/api/report/58362185a7a7f10843133337/')
        def mass_mock_get_invalid_data(url, request):
            self.assertEqual(request.headers['Authorization'], 'APIKEY {}'.format(self.api_key))
            return json.dumps(data)

        with HTTMock(mass_mock_get_invalid_data):
            ma = MASSApi(api_key=self.api_key, base_url=self.base_url)
            self.assertRaises(ValueError, lambda: ma.get_report('58362185a7a7f10843133337'))
