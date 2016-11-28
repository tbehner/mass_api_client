from tests.schema_test_case import SchemaTestCase
from mass_api_client.schemas.analysis_request import AnalysisRequestSchema


class AnalysisReqestTestCase(SchemaTestCase):
    def test_is_data_correct_after_serialization(self):
        data = {
            "analysis_requested": "2016-11-26T14:38:24+00:00",
            "analysis_system": "http://localhost:5000/api/analysis_system/strings/",
            "id": "58399e60a7a7f10cada00463",
            "priority": 0,
            "sample": "http://localhost:5000/api/sample/58399e60a7a7f10cada00461/",
            "url": "http://localhost:5000/api/analysis_request/58399e60a7a7f10cada00463/"
        }

        schema = AnalysisRequestSchema()
        self.assertEqualAfterSerialization(schema, data)
