from mass_api_client.schemas import AnalysisSystemInstanceSchema
from .base import BaseResource


class AnalysisSystemInstance(BaseResource):
    schema = AnalysisSystemInstanceSchema()

    def __repr__(self):
        return '[AnalysisSystemInstance] {}'.format(self.uuid)

    def __str__(self):
        return self.__repr__()

    def get(self, uuid):
        return self._get_detail_from_url("analysis_system_instance/{}/".format(uuid))
