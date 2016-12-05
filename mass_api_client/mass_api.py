import json

import requests

from mass_api_client.schemas.analysis_system import AnalysisSystemSchema
from mass_api_client.schemas.analysis_system_instance import AnalysisSystemInstanceSchema
from mass_api_client.schemas.report import ReportSchema
from mass_api_client.schemas.scheduled_analysis import ScheduledAnalysisSchema


class MASSApi:
    def __init__(self, api_key, base_url):
        self._api_key = api_key
        self._base_url = base_url
        self._default_headers = {'content-type': 'application/json',
                                 'Authorization': 'APIKEY {}'.format(api_key)}

    def _get_object(self, schema, url, many=False):
        response = self._get_json(url)
        serialized, errors = schema().load(response["results"] if many else response, many=many)

        if errors:
            raise ValueError("An error occurred during object deserialization: {}".format(errors))

        return serialized

    def _get_json(self, url):
        r = requests.get(url, headers=self._default_headers)
        r.raise_for_status()
        return r.json()

    def _post_json(self, url, data):
        r = requests.post(url, json.dumps(data), headers=self._default_headers)
        r.raise_for_status()
        return r

    def get_analysis_system(self, identifier):
        url = "{}analysis_system/{}/".format(self._base_url, identifier)
        return self._get_object(AnalysisSystemSchema, url)

    def get_all_analysis_systems(self):
        url = "{}analysis_system/".format(self._base_url)
        return self._get_object(AnalysisSystemSchema, url, many=True)

    def get_analysis_system_instance(self, uuid):
        url = "{}analysis_system_instance/{}/".format(self._base_url, uuid)
        return self._get_object(AnalysisSystemInstanceSchema, url)

    def get_all_analysis_system_instances(self):
        url = "{}analysis_system_instance/".format(self._base_url)
        return self._get_object(AnalysisSystemInstanceSchema, url, many=True)

    def get_scheduled_analyses(self, instance_uuid):
        url = "{}analysis_system_instance/{}/scheduled_analyses/".format(self._base_url, instance_uuid)
        return self._get_object(ScheduledAnalysisSchema, url, many=True)

    def get_report(self, report_id):
        url = "{}report/{}/".format(self._base_url, report_id)
        return self._get_object(ReportSchema, url)
