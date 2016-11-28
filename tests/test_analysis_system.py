from tests.schema_test_case import SchemaTestCase
from mass_api_client.schemas.analysis_system import AnalysisSystemSchema


class AnalysisSystemTestCase(SchemaTestCase):
    def test_is_data_correct_after_serialization(self):
        data = {
            "id": "5835b97fa7a7f10843133196",
            "identifier_name": "strings",
            "information_text": None,
            "tag_filter_expression": "",
            "url": "http://localhost:5000/api/analysis_system/strings/",
            "verbose_name": "Strings"
        }

        schema = AnalysisSystemSchema()
        self.assertEqualAfterSerialization(schema, data)
