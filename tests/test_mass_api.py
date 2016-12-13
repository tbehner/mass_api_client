import json
import unittest

import requests
from httmock import urlmatch, HTTMock

from mass_api_client import ConnectionManager


class MASSApiTestCase(unittest.TestCase):
    def setUp(self):
        self.api_key = '1234567890abcdef'
        self.base_url = 'http://localhost/api/'
        self.example_data = {'lorem': 'ipsum', 'integer': 1}
        self.cm = ConnectionManager()
        self.cm.register_connection(api_key=self.api_key, base_url=self.base_url, alias='default')

    def test_getting_json(self):
        @urlmatch(netloc=r'localhost', path=r'/api/json')
        def mass_mock_get_json(url, request):
            self.assertEqual(request.headers['Authorization'], 'APIKEY {}'.format(self.api_key))
            return json.dumps(self.example_data)

        with HTTMock(mass_mock_get_json):
            response = self.cm.get_json('http://localhost/api/json')

        self.assertEqual(self.example_data, response)

    def test_posting_json(self):
        @urlmatch(netloc=r'localhost', path=r'/api/json')
        def mass_mock_post_json(url, request):
            self.assertEqual(request.headers['Authorization'], 'APIKEY {}'.format(self.api_key))
            self.assertEqual(json.loads(request.body), self.example_data)
            return json.dumps(self.example_data)

        with HTTMock(mass_mock_post_json):
            response = self.cm.post_json('http://localhost/api/json', data=self.example_data)

        self.assertEqual(self.example_data, response.json())

    def test_receiving_server_error(self):
        @urlmatch(netloc=r'localhost', path=r'/api/json')
        def mass_mock_forbidden(url, request):
            return {'status_code': 403,
                    'content': json.dumps('{"error": "Access denied"}')}

        with HTTMock(mass_mock_forbidden):
            self.assertRaises(requests.exceptions.HTTPError, lambda: self.cm.get_json('http://localhost/api/json'))
            self.assertRaises(requests.exceptions.HTTPError, lambda: self.cm.post_json('http://localhost/api/json', self.example_data))

