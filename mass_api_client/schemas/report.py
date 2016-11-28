from marshmallow import fields, validate, post_load
from mass_api_client import Report
from .base import BaseSchema


class ReportSchema(BaseSchema):
    analysis_system = fields.Url(required=True)
    sample = fields.Url(required=True)
    analysis_date = fields.DateTime()
    upload_date = fields.DateTime(required=True)
    status = fields.Int(validate=validate.OneOf(Report.REPORT_STATUS_CODES))
    error_message = fields.Str(allow_none=True)
    tags = fields.List(cls_or_instance=fields.Str)
    additional_metadata = fields.Dict()
    json_report_objects = fields.Dict()
    raw_report_objects = fields.Dict()

    @post_load
    def make_object(self, data):
        return Report(**data)
