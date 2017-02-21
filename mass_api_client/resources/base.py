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
    default_filters = {}

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
    def _get_detail_from_url(cls, url, append_base_url=True):
        cm = ConnectionManager()

        deserialized = cls._deserialize(cm.get_json(url, append_base_url=append_base_url))
        return cls._create_instance_from_data(deserialized)

    @classmethod
    def _get_iter_from_url(cls, url, params={}, append_base_url=True):
        cm = ConnectionManager()
        next_url = url

        while next_url is not None:
            res = cm.get_json(next_url, params=params, append_base_url=append_base_url)
            deserialized = cls._deserialize(res['results'], many=True)
            for data in deserialized:
                yield cls._create_instance_from_data(data)
            try:
                next_url = res['next']
            except KeyError:
                raise StopIteration
            append_base_url = False

    @classmethod
    def _get_list_from_url(cls, url, params=None, append_base_url=True):
        if params is None:
            params = {}

        cm = ConnectionManager()
        deserialized = cls._deserialize(cm.get_json(url, params=params, append_base_url=append_base_url)['results'], many=True)
        objects = [cls._create_instance_from_data(detail) for detail in deserialized]

        return objects

    @classmethod
    def _create(cls, additional_json_files=None, additional_binary_files=None, url=None, **kwargs):
        cm = ConnectionManager()
        if not url:
            url = '{}/'.format(cls.creation_point)
        serialized, errors = cls.schema.dump(kwargs)

        if additional_binary_files or additional_json_files:
            response_data = cm.post_multipart(url, serialized, json_files=additional_json_files, binary_files=additional_binary_files)
        else:
            response_data = cm.post_json(url, serialized)

        deserialized = cls._deserialize(response_data)

        return cls._create_instance_from_data(deserialized)

    @classmethod
    def get(cls, identifier):
        return cls._get_detail_from_url('{}/{}/'.format(cls.endpoint, identifier))

    @classmethod
    def items(cls):
        return cls._get_iter_from_url('{}/'.format(cls.endpoint), params=cls.default_filters)

    @classmethod
    def all(cls):
        return cls._get_list_from_url('{}/'.format(cls.endpoint), params=cls.default_filters)

    @classmethod
    def query(cls, **kwargs):
        params = cls.default_filters

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
