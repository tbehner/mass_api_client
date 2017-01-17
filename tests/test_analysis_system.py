import json

from mass_api_client.resources import AnalysisSystem
from tests.serialization_test_case import SerializationTestCase


class AnalysisSystemTestCase(SerializationTestCase):
    def test_is_data_correct_after_serialization(self):
        with open('tests/data/analysis_system.json') as data_file:
            data = json.load(data_file)

        self.assertEqualAfterSerialization(AnalysisSystem, data)
