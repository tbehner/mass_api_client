import json

from mass_api_client.schemas.analysis_system_instance import AnalysisSystemInstanceSchema
from tests.schema_test_case import SchemaTestCase


class AnalysisSystemInstanceTestCase(SchemaTestCase):
    def test_is_data_correct_after_serialization(self):
        with open('tests/data/analysis_system_instance.json') as data_file:
            data = json.load(data_file)

        schema = AnalysisSystemInstanceSchema()
        self.assertEqualAfterSerialization(schema, data)
