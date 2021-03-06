import json
import tempfile

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
            response = self.cm.post_json('http://localhost/api/json', append_base_url=False, data=self.example_data)

        self.assertEqual(self.example_data, response)

    def test_posting_json_with_file(self):
        with open('tests/data/test_data', 'rb') as data_file:
            @urlmatch(netloc=r'localhost', path=r'/api/json')
            def mass_mock_post_file(url, request):
                self.assertAuthorized(request)
                self.assertHasFile(request, 'file', 'test_data', data_file)
                self.assertHasForm(request, 'metadata', json.dumps(self.example_data), 'application/json')
                return json.dumps(self.example_data)

            with HTTMock(mass_mock_post_file):
                files = {'file': ('test_data', data_file)}
                response = self.cm.post_multipart('http://localhost/api/json', append_base_url=False,
                                                  metadata=self.example_data, binary_files=files)

        self.assertEqual(self.example_data, response)

    def test_receiving_server_error(self):
        @urlmatch(netloc=r'localhost', path=r'/api/json')
        def mass_mock_forbidden(url, request):
            return {'status_code': 403,
                    'content': json.dumps('{"error": "Access denied"}')}

        with HTTMock(mass_mock_forbidden):
            self.assertRaises(requests.exceptions.HTTPError,
                              lambda: self.cm.get_json('http://localhost/api/json', append_base_url=False))
            self.assertRaises(requests.exceptions.HTTPError,
                              lambda: self.cm.post_json('http://localhost/api/json', self.example_data,
                                                        append_base_url=False))

    def test_downloading_file(self):
        test_file_path = 'tests/data/test_data'

        @urlmatch(netloc=r'localhost', path=r'/api/file')
        def mass_mock_file(url, request):
            self.assertAuthorized(request)
            with open(test_file_path, 'rb') as data_file:
                content = data_file.read()
            return content

        with HTTMock(mass_mock_file), tempfile.TemporaryFile() as tmpfile, open(test_file_path, 'rb') as data_file:
            self.cm.download_to_file('file', tmpfile)
            tmpfile.seek(0)
            self.assertEqual(data_file.read(), tmpfile.read())
