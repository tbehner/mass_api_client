from marshmallow import fields

from .base import BaseSchema


class AnalysisRequestSchema(BaseSchema):
    analysis_system = fields.Url(required=True)
    sample = fields.Url(required=True)
    analysis_requested = fields.DateTime(required=True)
    priority = fields.Int(default=0, required=True)
