import json

from mass_api_client.schemas.analysis_request import AnalysisRequestSchema
from tests.schema_test_case import SchemaTestCase


class AnalysisReqestTestCase(SchemaTestCase):
    def test_is_data_correct_after_serialization(self):
        with open('tests/data/analysis_request.json') as data_file:
            data = json.load(data_file)

        schema = AnalysisRequestSchema()
        self.assertEqualAfterSerialization(schema, data)
