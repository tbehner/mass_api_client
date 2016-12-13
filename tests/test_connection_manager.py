import json

import requests
from httmock import urlmatch, HTTMock

from tests.httmock_test_case import HTTMockTestCase


class MASSApiTestCase(HTTMockTestCase):
    def test_getting_json(self):
        @urlmatch(netloc=r'localhost', path=r'/api/json')
        def mass_mock_get_json(url, request):
            self.assertAuthorized(request)
            return json.dumps(self.example_data)

        with HTTMock(mass_mock_get_json):
            response = self.cm.get_json('http://localhost/api/json', append_base_url=False)

        self.assertEqual(self.example_data, response)

    def test_posting_json(self):
        @urlmatch(netloc=r'localhost', path=r'/api/json')
        def mass_mock_post_json(url, request):
            self.assertAuthorized(request)
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
            self.assertRaises(requests.exceptions.HTTPError, lambda: self.cm.get_json('http://localhost/api/json', append_base_url=False))
            self.assertRaises(requests.exceptions.HTTPError, lambda: self.cm.post_json('http://localhost/api/json', self.example_data))

