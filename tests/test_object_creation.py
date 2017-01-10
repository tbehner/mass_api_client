import json

from httmock import urlmatch, HTTMock

from mass_api_client.resources import *
from tests.httmock_test_case import HTTMockTestCase


class ObjectCreationTestCase(HTTMockTestCase):
    def assertCorrectHTTPDetailCreation(self, resource, path, data, data_path):
        with open(data_path) as data_file:
            response_data = json.load(data_file)

        @urlmatch(netloc=r'localhost', path=path)
        def mass_mock_creation(url, request):
            self.assertAuthorized(request)
            self.assertEqual(json.loads(request.body), data)
            return json.dumps(response_data)

        with HTTMock(mass_mock_creation):
            obj = resource.create(**data)
            self.assertEqual(response_data, obj._to_json())

    def assertCorrectHTTPDetailCreationWithFile(self, resource, path, metadata, data_path, filename, file):
        with open(data_path) as data_file:
            response_data = json.load(data_file)

        @urlmatch(netloc=r'localhost', path=path)
        def mass_mock_creation(url, request):
            self.assertAuthorized(request)
            self.assertHasFile(request, 'file', filename, file)
            self.assertHasFile(request, 'metadata', 'metadata', json.dumps(metadata), content_type='application/json')
            return json.dumps(response_data)

        with HTTMock(mass_mock_creation):
            obj = resource.create(filename=filename, file=file, **metadata)
            self.assertEqual(response_data, obj._to_json())

    def test_creating_analysis_system(self):
        data = {'identifier_name': 'identifier', 'verbose_name': 'Verbose name', 'tag_filter_expression': ''}
        self.assertCorrectHTTPDetailCreation(AnalysisSystem, r'/api/analysis_system/', data,
                                             'tests/data/analysis_system.json')

    def test_creating_analysis_system_instance(self):
        data = {'analysis_system': 'http://localhost/api/analysis_system/strings/'}
        self.assertCorrectHTTPDetailCreation(AnalysisSystemInstance, r'/api/analysis_system_instance/', data,
                                             'tests/data/analysis_system_instance.json')

    def test_creating_scheduled_analysis(self):
        data = {
            'analysis_system_instance': 'http://localhost/api/analysis_system_instance/5a391093-f251-4c08-991d-26fc5e0e5793/',
            'sample': 'http://localhost:5000/api/sample/580a2429a7a7f126d0cc0d10/'}
        self.assertCorrectHTTPDetailCreation(ScheduledAnalysis, r'/api/scheduled_analysis/', data,
                                             'tests/data/scheduled_analysis.json')

    def test_creating_domain_sample(self):
        data = {'domain': 'uni-bonn.de', 'tlp_level': 0}
        self.assertCorrectHTTPDetailCreation(DomainSample, r'/api/sample/submit_domain/', data,
                                             'tests/data/domain_sample.json')

    def test_creating_ip_sample(self):
        data = {'ip_address': '192.168.1.1', 'tlp_level': 0}
        self.assertCorrectHTTPDetailCreation(IPSample, r'/api/sample/submit_ip/', data,
                                             'tests/data/ip_sample.json')

    def test_creating_uri_sample(self):
        data = {'uri': 'http://uni-bonn.de/test', 'tlp_level': 0}
        self.assertCorrectHTTPDetailCreation(URISample, r'/api/sample/submit_uri/', data, 'tests/data/uri_sample.json')

    def test_creating_file_sample(self):
        with open('tests/data/test_data', 'rb') as file:
            data = {'tlp_level': 0}
            self.assertCorrectHTTPDetailCreationWithFile(FileSample, r'/api/sample/submit_file/', data,
                                                         'tests/data/ip_sample.json', 'test_data', file)
