import json

from mass_api_client.schemas.sample import DomainSampleSchema, IPSampleSchema, FileSampleSchema, ExecutableBinarySampleSchema
from tests.schema_test_case import SchemaTestCase


class DomainSampleTestCase(SchemaTestCase):
    def test_is_data_correct_after_serialization(self):
        with open('tests/data/domain_sample.json') as data_file:
            data = json.load(data_file)

        schema = DomainSampleSchema()
        self.assertEqualAfterSerialization(schema, data)


class IPSampleTestCase(SchemaTestCase):
    def test_is_data_correct_after_serialization(self):
        with open('tests/data/ip_sample.json') as data_file:
            data = json.load(data_file)

        schema = IPSampleSchema()
        self.assertEqualAfterSerialization(schema, data)


class FileSampleTestCase(SchemaTestCase):
    def test_is_data_correct_after_serialization(self):
        with open('tests/data/file_sample.json') as data_file:
            data = json.load(data_file)

        schema = FileSampleSchema()
        self.assertEqualAfterSerialization(schema, data)


class ExecutableBinarySampleTestCase(SchemaTestCase):
    def test_is_data_correct_after_serialization(self):
        with open('tests/data/executable_binary_sample.json') as data_file:
            data = json.load(data_file)

        schema = ExecutableBinarySampleSchema()
        self.assertEqualAfterSerialization(schema, data)
