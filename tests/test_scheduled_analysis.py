import json

from mass_api_client.schemas.scheduled_analysis import ScheduledAnalysisSchema
from tests.schema_test_case import SchemaTestCase


class ScheduledAnalysisTestCase(SchemaTestCase):
    def test_is_data_correct_after_serialization(self):
        with open('tests/data/scheduled_analysis.json') as data_file:
            data = json.load(data_file)

        schema = ScheduledAnalysisSchema()
        self.assertEqualAfterSerialization(schema, data)
