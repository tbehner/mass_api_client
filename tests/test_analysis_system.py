import json

from mass_api_client.schemas.analysis_system import AnalysisSystemSchema
from tests.schema_test_case import SchemaTestCase


class AnalysisSystemTestCase(SchemaTestCase):
    def test_is_data_correct_after_serialization(self):
        with open('tests/data/analysis_system.json') as data_file:
            data = json.load(data_file)

        schema = AnalysisSystemSchema()
        self.assertEqualAfterSerialization(schema, data)
