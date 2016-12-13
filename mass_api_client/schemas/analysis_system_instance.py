from marshmallow import fields, validate

from .base import BaseSchema


class AnalysisSystemInstanceSchema(BaseSchema):
    analysis_system = fields.Url(required=True)
    uuid = fields.Str(validate=validate.Length(max=36), required=True)
    last_seen = fields.DateTime(allow_none=True)
    is_online = fields.Bool()
    scheduled_analyses_count = fields.Int()
