from tests.schema_test_case import SchemaTestCase
from mass_api_client.schemas.scheduled_analysis import ScheduledAnalysisSchema


class ScheduledAnalysisTestCase(SchemaTestCase):
    def test_is_data_correct_after_serialization(self):
        data = {
            "analysis_scheduled": "2016-11-24T00:38:21+00:00",
            "analysis_system_instance": "http://localhost:5000/api/analysis_system_instance/b200ad66-f18a-4b37-b251-91d5ee948ef4/",
            "id": "5836367da7a7f1084313338d",
            "priority": 0,
            "sample": "http://localhost:5000/api/sample/583621b9a7a7f1084313337a/",
            "url": "http://localhost:5000/api/scheduled_analysis/5836367da7a7f1084313338d/"
        }

        schema = ScheduledAnalysisSchema()
        self.assertEqualAfterSerialization(schema, data)
