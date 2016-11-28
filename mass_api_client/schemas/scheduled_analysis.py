from marshmallow import fields, post_load
from mass_api_client import ScheduledAnalysis
from .base import BaseSchema


class ScheduledAnalysisSchema(BaseSchema):
    analysis_system_instance = fields.Url(required=True)
    sample = fields.Url(required=True)
    analysis_scheduled = fields.DateTime(required=True)
    priority = fields.Int(default=0, required=True)

    @post_load
    def make_object(self, data):
        return ScheduledAnalysis(**data)
