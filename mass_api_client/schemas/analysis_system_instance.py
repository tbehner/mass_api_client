from marshmallow import fields, validate, post_load
from mass_api_client.analysis_system_instance import AnalysisSystemInstance
from .base import BaseSchema


class AnalysisSystemInstanceSchema(BaseSchema):
    analysis_system = fields.Url(required=True)
    uuid = fields.Str(validate=validate.Length(max=36), required=True)
    last_seen = fields.DateTime(allow_none=True)
    is_online = fields.Bool()
    scheduled_analyses_count = fields.Int()

    @post_load
    def make_object(self, data):
        return AnalysisSystemInstance(**data)
