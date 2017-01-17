import json

from mass_api_client.resources import Report
from tests.serialization_test_case import SerializationTestCase


class ReportTestCase(SerializationTestCase):
    def test_is_data_correct_after_serialization(self):
        with open('tests/data/report.json') as data_file:
            data = json.load(data_file)

        self.assertEqualAfterSerialization(Report, data)
