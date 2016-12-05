from marshmallow import fields, validate, post_load

from mass_api_client.resources.sample import DomainSample, IPSample, FileSample, ExecutableBinarySample
from .base import BaseSchema


class SampleSchema(BaseSchema):
    delivery_date = fields.DateTime(required=True)
    first_seen = fields.DateTime(required=True)
    tags = fields.List(cls_or_instance=fields.Str)
    dispatched_to = fields.List(cls_or_instance=fields.Str)
    tlp_level = fields.Int(required=True)


class DomainSampleSchema(SampleSchema):
    _cls = fields.Str(validate=validate.Equal("Sample.DomainSample"))
    domain = fields.Str()

    @post_load
    def make_object(self, data):
        return DomainSample(**data)


class IPSampleSchema(SampleSchema):
    _cls = fields.Str(validate=validate.Equal("Sample.IPSample"))
    ip_address = fields.Str()

    @post_load
    def make_object(self, data):
        return IPSample(**data)


class FileSampleSchema(SampleSchema):
    _cls = fields.Str(validate=validate.Equal("Sample.FileSample"))
    file = fields.Str()
    file_names = fields.List(cls_or_instance=fields.Str)
    file_size = fields.Int()
    magic_string = fields.Str()
    mime_type = fields.Str()
    md5sum = fields.Str(required=True, validate=validate.Length(equal=32))
    sha1sum = fields.Str(required=True, validate=validate.Length(equal=40))
    sha256sum = fields.Str(required=True, validate=validate.Length(equal=64))
    sha512sum = fields.Str(required=True, validate=validate.Length(equal=128))
    ssdeep_hash = fields.Str(required=True, validate=validate.Length(max=200))
    shannon_entropy = fields.Float(validate=validate.Range(min=0, max=8))

    @post_load
    def make_object(self, data):
        return FileSample(**data)


class ExecutableBinarySampleSchema(FileSampleSchema):
    _cls = fields.Str(validate=validate.Equal("Sample.FileSample.ExecutableBinarySample"))
    filesystem_events = fields.List(cls_or_instance=fields.Str)
    registry_events = fields.List(cls_or_instance=fields.Str)
    sections = fields.List(cls_or_instance=fields.Str)
    resources = fields.List(cls_or_instance=fields.Str)
    imports = fields.List(cls_or_instance=fields.Str)
    strings = fields.List(cls_or_instance=fields.Str)

    @post_load
    def make_object(self, data):
        return ExecutableBinarySample(**data)