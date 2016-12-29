from mass_api_client.schemas import DomainSampleSchema, IPSampleSchema, FileSampleSchema, ExecutableBinarySampleSchema
from .base import BaseResource


class Sample(BaseResource):
    endpoint = 'sample'

    @classmethod
    def _create_instance_from_data(cls, data):
        subcls = sample_classes[data['_cls']]
        return subcls(**data)

    @classmethod
    def _deserialize(cls, data, many=False):
        if many:
            return [cls._deserialize(item) for item in data]

        subcls = sample_classes[data['_cls']]
        return super(Sample, subcls)._deserialize(data, many)

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

sample_classes = {
                    'Sample.DomainSample': DomainSample,
                    'Sample.IPSample': IPSample,
                    'Sample.FileSample': FileSample,
                    'Sample.FileSample.ExecutableBinarySample': ExecutableBinarySample
                  }
