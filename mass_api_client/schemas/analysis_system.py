from marshmallow import fields, validate, post_load
from mass_api_client.resources.analysis_system import AnalysisSystem
from .base import BaseSchema


class AnalysisSystemSchema(BaseSchema):
    identifier_name = fields.Str(validate=validate.Length(min=3, max=50), required=True)
    verbose_name = fields.Str(validate=validate.Length(max=200), required=True)
    information_text = fields.Str(allow_none=True)
    tag_filter_expression = fields.Str(validate=validate.Length(max=400), default='', required=True)

    @post_load
    def make_object(self, data):
        return AnalysisSystem(**data)
