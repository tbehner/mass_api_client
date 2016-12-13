from mass_api_client.connection_manager import ConnectionManager


class Ref:
    def __init__(self, key):
        self.key = key

    def resolve(self, obj):
        return getattr(obj, self.key, None)


class BaseResource:
    schema = None

    @property
    def schema(self):
        return Ref('schema').resolve(self)

    def get_detail_from_url(self, url):
        cm = ConnectionManager()
        return self.get_detail_from_json(cm.get_json(url))

    def get_detail_from_json(self, data):
        deserialized, errors = self.schema.load(data)

        if errors:
            raise ValueError('An error occurred during object deserialization: {}'.format(errors))

        self.__dict__.update(deserialized)
        return self

    def to_json(self):
        serialized, errors = self.schema.dump(self)

        if errors:
            raise ValueError('An error occurred during object serialization: {}'.format(errors))

        return serialized
