from marshmallow import fields, post_load
from mass_api_client import AnalysisRequest
from .base import BaseSchema


class AnalysisRequestSchema(BaseSchema):
    analysis_system = fields.Url(required=True)
    sample = fields.Url(required=True)
    analysis_requested = fields.DateTime(required=True)
    priority = fields.Int(default=0, required=True)

    @post_load
    def make_object(self, data):
        return AnalysisRequest(**data)
