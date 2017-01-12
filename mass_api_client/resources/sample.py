from mass_api_client.resources import Report
from mass_api_client.schemas import DomainSampleSchema, IPSampleSchema, URISampleSchema, FileSampleSchema, ExecutableBinarySampleSchema
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

    def get_reports(self):
        url = '{}reports/'.format(self.url)
        return Report._get_list_from_url(url, append_base_url=False)

    def __repr__(self):
        return '[{}] {}'.format(str(self.__class__.__name__), str(self.id))

    def __str__(self):
        return self.__repr__()


class DomainSample(Sample):
    schema = DomainSampleSchema()
    creation_point = 'sample/submit_domain'
    default_filters = {'_cls': 'Sample.DomainSample'}

    @classmethod
    def create(cls, domain, tlp_level=0):
        return cls._create(domain=domain, tlp_level=tlp_level)


class URISample(Sample):
    schema = URISampleSchema()
    creation_point = 'sample/submit_uri'
    default_filters = {'_cls': 'Sample.URISample'}

    @classmethod
    def create(cls, uri, tlp_level=0):
        return cls._create(uri=uri, tlp_level=tlp_level)


class IPSample(Sample):
    schema = IPSampleSchema()
    creation_point = 'sample/submit_ip'
    default_filters = {'_cls': 'Sample.IPSample'}

    @classmethod
    def create(cls, ip_address, tlp_level=0):
        return cls._create(ip_address=ip_address, tlp_level=tlp_level)


class FileSample(Sample):
    schema = FileSampleSchema()
    creation_point = 'sample/submit_file'
    default_filters = {'_cls__startswith': 'Sample.FileSample'}

    filter_parameters = [
        'md5sum',
        'sha1sum',
        'sha256sum',
        'sha512sum'
    ]

    @classmethod
    def create(cls, filename, file, tlp_level=0):
        return cls._create(additional_binary_files={'file': (filename, file)}, tlp_level=tlp_level)


class ExecutableBinarySample(FileSample):
    schema = ExecutableBinarySampleSchema()
    default_filters = {'_cls': 'Sample.FileSample.ExecutableBinarySample'}

sample_classes = {
                    'Sample.DomainSample': DomainSample,
                    'Sample.IPSample': IPSample,
                    'Sample.URISample': URISample,
                    'Sample.FileSample': FileSample,
                    'Sample.FileSample.ExecutableBinarySample': ExecutableBinarySample
                  }
