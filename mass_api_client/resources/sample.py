from mass_api_client.schemas import DomainSampleSchema, IPSampleSchema, FileSampleSchema, ExecutableBinarySampleSchema
from .base import BaseResource


class Sample(BaseResource):
    def __repr__(self):
        return '[{}] {}'.format(str(self.__class__.__name__), str(self.id))

    def __str__(self):
        return self.__repr__()


class DomainSample(Sample):
    schema = DomainSampleSchema()


class IPSample(Sample):
    schema = IPSampleSchema()


class FileSample(Sample):
    schema = FileSampleSchema()


class ExecutableBinarySample(FileSample):
    schema = ExecutableBinarySampleSchema()
