from tests.schema_test_case import SchemaTestCase
from mass_api_client.schemas.report import ReportSchema


class ReportTestCase(SchemaTestCase):
    def test_is_data_correct_after_serialization(self):
        data = {
            "additional_metadata": {
                "number_of_strings": 564913
            },
            "analysis_date": "2016-11-23T15:59:52+00:00",
            "analysis_system": "http://localhost:5000/api/analysis_system/strings/",
            "error_message": None,
            "id": "5835bd5ca7a7f108431331d0",
            "json_report_objects": {
                "found_strings": "http://localhost:5000/api/report/5835bd5ca7a7f108431331d0/json_report_object/found_strings/"
            },
            "raw_report_objects": {},
            "sample": "http://localhost:5000/api/sample/5822057fa7a7f10cc420e3b7/",
            "status": 0,
            "tags": [],
            "upload_date": "2016-11-23T16:01:32+00:00",
            "url": "http://localhost:5000/api/report/5835bd5ca7a7f108431331d0/"
        }

        schema = ReportSchema()

        self.assertEqualAfterSerialization(schema, data)
