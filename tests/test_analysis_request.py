import json

from mass_api_client.resources import AnalysisRequest
from tests.serialization_test_case import SerializationTestCase


class AnalysisReqestTestCase(SerializationTestCase):
    def test_is_data_correct_after_serialization(self):
        with open('tests/data/analysis_request.json') as data_file:
            data = json.load(data_file)

        self.assertEqualAfterSerialization(AnalysisRequest(), data)
