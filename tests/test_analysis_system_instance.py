from tests.schema_test_case import SchemaTestCase
from mass_api_client.schemas.analysis_system_instance import AnalysisSystemInstanceSchema


class AnalysisSystemInstanceTestCase(SchemaTestCase):
    def test_is_data_correct_after_serialization(self):
        data = {
            "analysis_system": "http://localhost:5000/api/analysis_system/croax/",
            "id": "5834ae94a7a7f11e52b06287",
            "is_online": False,
            "last_seen": None,
            "scheduled_analyses_count": 0,
            "url": "http://localhost:5000/api/analysis_system_instance/5a391093-f251-4c08-991d-26fc5e0e5793/",
            "uuid": "5a391093-f251-4c08-991d-26fc5e0e5793"
        }

        schema = AnalysisSystemInstanceSchema()
        self.assertEqualAfterSerialization(schema, data)
