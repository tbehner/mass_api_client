import json

from mass_api_client.resources import DomainSample, IPSample, URISample, FileSample, ExecutableBinarySample
from tests.serialization_test_case import SerializationTestCase


class DomainSampleTestCase(SerializationTestCase):
    def test_is_data_correct_after_serialization(self):
        with open('tests/data/domain_sample.json') as data_file:
            data = json.load(data_file)

        self.assertEqualAfterSerialization(DomainSample, data)


class IPSampleTestCase(SerializationTestCase):
    def test_is_data_correct_after_serialization(self):
        with open('tests/data/ip_sample.json') as data_file:
            data = json.load(data_file)

        self.assertEqualAfterSerialization(IPSample, data)


class URISampleTestCase(SerializationTestCase):
    def test_is_data_correct_after_serialization(self):
        with open('tests/data/uri_sample.json') as data_file:
            data = json.load(data_file)

        self.assertEqualAfterSerialization(URISample, data)


class FileSampleTestCase(SerializationTestCase):
    def test_is_data_correct_after_serialization(self):
        with open('tests/data/file_sample.json') as data_file:
            data = json.load(data_file)

        self.assertEqualAfterSerialization(FileSample, data)


class ExecutableBinarySampleTestCase(SerializationTestCase):
    def test_is_data_correct_after_serialization(self):
        with open('tests/data/executable_binary_sample.json') as data_file:
            data = json.load(data_file)

        self.assertEqualAfterSerialization(ExecutableBinarySample, data)
