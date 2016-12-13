import unittest


class SerializationTestCase(unittest.TestCase):
    def assertEqualAfterSerialization(self, resource, data):
        self.maxDiff = None

        obj = resource._get_detail_from_json(data)
        serialized = obj._to_json()

        self.assertDictEqual(data, serialized)
