import unittest


class SerializationTestCase(unittest.TestCase):
    def assertEqualAfterSerialization(self, resource, data):
        self.maxDiff = None

        obj, errors_load = resource.schema.load(data)
        serialized, errors_dump = resource.schema.dump(obj)

        self.assertEqual({}, errors_load)
        self.assertEqual({}, errors_dump)
        self.assertDictEqual(data, serialized)
