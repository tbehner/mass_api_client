import json

import requests


class Connection:
    def __init__(self, api_key, base_url):
        self._api_key = api_key
        self._base_url = base_url
        self._default_headers = {'content-type': 'application/json',
                                 'Authorization': 'APIKEY {}'.format(api_key)}

    def get_json(self, url, append_base_url, params):
        if append_base_url:
            url = self._base_url + url

        r = requests.get(url, headers=self._default_headers, params=params)
        r.raise_for_status()
        return r.json()

    def post_json(self, url, data, append_base_url, params, file):
        if append_base_url:
            url = self._base_url + url

        if file:
            headers = {'Authorization': self._default_headers['Authorization']}
            request_body = {'metadata': (None, json.dumps(data), 'application/json'), 'file': file}
            r = requests.post(url, headers=headers, params=params, files=request_body)
        else:
            r = requests.post(url, json.dumps(data), headers=self._default_headers, params=params)

        r.raise_for_status()
        return r.json()


class ConnectionManager:
    _connections = {}

    def register_connection(self, alias, api_key, base_url):
        self._connections[alias] = Connection(api_key, base_url)

    def get_json(self, url, append_base_url=True, params={}):
        return self._connections['default'].get_json(url, append_base_url, params)

    def post_json(self, url, data, append_base_url=True, params={}, file=None):
        return self._connections['default'].post_json(url, data, append_base_url, params, file)
