from tests.schema_test_case import SchemaTestCase
from mass_api_client.schemas.report import ReportSchema


class ReportTestCase(SchemaTestCase):
    def test_is_data_correct_after_serialization(self):
        data = {
            "additional_metadata": {
                "number_of_strings": 44155
            },
            "analysis_date": "2016-11-23T20:23:15.545000+00:00",
            "analysis_system": "http://localhost:5000/api/analysis_system/strings/",
            "error_message": None,
            "id": "58362185a7a7f10843133337",
            "json_report_objects": {
                "found_strings": "http://localhost:5000/api/report/58362185a7a7f10843133337/json_report_object/found_strings/"
            },
            "raw_report_objects": {},
            "sample": "http://localhost:5000/api/sample/58362178a7a7f1084313332b/",
            "status": 0,
            "tags": [],
            "upload_date": "2016-11-23T23:08:53+00:00",
            "url": "http://localhost:5000/api/report/58362185a7a7f10843133337/"
        }

        schema = ReportSchema()

        self.assertEqualAfterSerialization(schema, data)
