import unittest


class SerializationTestCase(unittest.TestCase):
    def assertEqualAfterSerialization(self, resource, data):
        self.maxDiff = None

        obj = resource.get_detail_from_json(data)
        serialized = obj.to_json()

        self.assertDictEqual(data, serialized)
