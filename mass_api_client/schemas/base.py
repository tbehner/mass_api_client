from marshmallow import Schema, fields


class BaseSchema(Schema):
    id = fields.Str()
    url = fields.Url()
