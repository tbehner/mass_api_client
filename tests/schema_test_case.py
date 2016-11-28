import unittest


class SchemaTestCase(unittest.TestCase):
    def assertEqualAfterSerialization(self, schema, data):
        self.maxDiff = None

        deserialized, errors_load = schema.load(data)
        serialized, errors_dump = schema.dump(deserialized)

        self.assertEqual(errors_load, {})
        self.assertEqual(errors_dump, {})
        self.assertDictEqual(data, serialized)
