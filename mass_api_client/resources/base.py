from mass_api_client.connection_manager import ConnectionManager


class Ref:
    def __init__(self, key):
        self.key = key

    def resolve(self, obj):
        return getattr(obj, self.key, None)


class BaseResource:
    schema = None
    endpoint = None
    creation_point = None
    filter_parameters = []

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
    def _get_list_from_url(cls, url, params={}):
        cm = ConnectionManager()

        deserialized = cls._deserialize(cm.get_json(url, params=params)['results'], many=True)
        objects = [cls._create_instance_from_data(detail) for detail in deserialized]

        return objects

    @classmethod
    def _create(cls, additional_file=None, **kwargs):
        cm = ConnectionManager()
        url = '{}/'.format(cls.creation_point)
        serialized, errors = cls.schema.dump(kwargs)

        if additional_file:
            response_data = cm.post_json(url, serialized, file=additional_file)
        else:
            response_data = cm.post_json(url, serialized)

        deserialized = cls._deserialize(response_data)

        return cls._create_instance_from_data(deserialized)

    @classmethod
    def get(cls, identifier):
        return cls._get_detail_from_url('{}/{}/'.format(cls.endpoint, identifier))

    @classmethod
    def all(cls):
        return cls._get_list_from_url('{}/'.format(cls.endpoint))

    @classmethod
    def query(cls, **kwargs):
        params = {}

        for key, value in kwargs.items():
            if key in cls.filter_parameters:
                params[key] = value
            else:
                raise ValueError('\'{}\' is not a filter parameter for class \'{}\''.format(key, cls.__name__))

        return cls._get_list_from_url('{}/'.format(cls.endpoint), params=params)

    def _to_json(self):
        serialized, errors = self.schema.dump(self)

        if errors:
            raise ValueError('An error occurred during object serialization: {}'.format(errors))

        return serialized
