from mass_api_client.connection_manager import ConnectionManager


class Ref:
    def __init__(self, key):
        self.key = key

    def resolve(self, obj):
        return getattr(obj, self.key, None)


class BaseResource:
    schema = None
    endpoint = None

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @classmethod
    @property
    def schema(cls):
        return Ref('schema').resolve(cls)

    @classmethod
    def _deserialize(cls, data, many=False):
        deserialized, errors = cls.schema.load(data, many=many)

        if errors:
            raise ValueError('An error occurred during object deserialization: {}'.format(errors))

        return deserialized

    @classmethod
    def _create_instance_from_data(cls, data):
        return cls(**data)

    @classmethod
    def _get_detail_from_url(cls, url):
        cm = ConnectionManager()

        deserialized = cls._deserialize(cm.get_json(url))
        return cls._create_instance_from_data(deserialized)

    @classmethod
    def _get_list_from_url(cls, url):
        cm = ConnectionManager()

        deserialized = cls._deserialize(cm.get_json(url)['results'], many=True)
        objects = [cls._create_instance_from_data(detail) for detail in deserialized]

        return objects

    @classmethod
    def get(cls, identifier):
        return cls._get_detail_from_url('{}/{}/'.format(cls.endpoint, identifier))

    @classmethod
    def all(cls):
        return cls._get_list_from_url('{}/'.format(cls.endpoint))

    def _to_json(self):
        serialized, errors = self.schema.dump(self)

        if errors:
            raise ValueError('An error occurred during object serialization: {}'.format(errors))

        return serialized
