import json

from mass_api_client.schemas.report import ReportSchema
from tests.schema_test_case import SchemaTestCase


class ReportTestCase(SchemaTestCase):
    def test_is_data_correct_after_serialization(self):
        with open('tests/data/report.json') as data_file:
            data = json.load(data_file)

        schema = ReportSchema()

        self.assertEqualAfterSerialization(schema, data)
