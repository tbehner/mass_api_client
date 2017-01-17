from mass_api_client.resources import Report
from mass_api_client.schemas import DomainSampleSchema, IPSampleSchema, URISampleSchema, FileSampleSchema, ExecutableBinarySampleSchema
from .base_with_subclasses import BaseWithSubclasses


class Sample(BaseWithSubclasses):
    endpoint = 'sample'
    _class_identifier = 'Sample'

    def get_reports(self):
        url = '{}reports/'.format(self.url)
        return Report._get_list_from_url(url, append_base_url=False)

    def __repr__(self):
        return '[{}] {}'.format(str(self.__class__.__name__), str(self.id))

    def __str__(self):
        return self.__repr__()


class DomainSample(Sample):
    schema = DomainSampleSchema()
    _class_identifier = 'Sample.DomainSample'
    creation_point = 'sample/submit_domain'
    default_filters = {'_cls': _class_identifier}

    @classmethod
    def create(cls, domain, tlp_level=0):
        return cls._create(domain=domain, tlp_level=tlp_level)


class URISample(Sample):
    schema = URISampleSchema()
    _class_identifier = 'Sample.URISample'
    creation_point = 'sample/submit_uri'
    default_filters = {'_cls': _class_identifier}

    @classmethod
    def create(cls, uri, tlp_level=0):
        return cls._create(uri=uri, tlp_level=tlp_level)


class IPSample(Sample):
    schema = IPSampleSchema()
    _class_identifier = 'Sample.IPSample'
    creation_point = 'sample/submit_ip'
    default_filters = {'_cls': _class_identifier}

    @classmethod
    def create(cls, ip_address, tlp_level=0):
        return cls._create(ip_address=ip_address, tlp_level=tlp_level)


class FileSample(Sample):
    schema = FileSampleSchema()
    _class_identifier = 'Sample.FileSample'
    creation_point = 'sample/submit_file'
    default_filters = {'_cls__startswith': _class_identifier}

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
    _class_identifier = 'Sample.FileSample.ExecutableBinarySample'
    default_filters = {'_cls': _class_identifier}

