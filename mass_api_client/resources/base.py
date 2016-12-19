from mass_api_client.connection_manager import ConnectionManager


class Ref:
    def __init__(self, key):
        self.key = key

    def resolve(self, obj):
        return getattr(obj, self.key, None)


class BaseResource:
    schema = None
    identifier = None

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @classmethod
    @property
    def schema(cls):
        return Ref('schema').resolve(cls)

    @classmethod
    def _get_detail_from_url(cls, url):
        cm = ConnectionManager()
        return cls._get_detail_from_json(cm.get_json(url))

    @classmethod
    def _get_detail_from_json(cls, data):
        deserialized, errors = cls.schema.load(data)

        if errors:
            raise ValueError('An error occurred during object deserialization: {}'.format(errors))

        return cls(**deserialized)

    @classmethod
    def get(cls, identifier):
        return cls._get_detail_from_url('{}/{}/'.format(cls.endpoint, identifier))

    def _to_json(self):
        serialized, errors = self.schema.dump(self)

        if errors:
            raise ValueError('An error occurred during object serialization: {}'.format(errors))

        return serialized
