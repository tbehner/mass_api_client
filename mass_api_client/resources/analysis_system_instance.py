from mass_api_client.schemas import AnalysisSystemInstanceSchema
from .base import BaseResource


class AnalysisSystemInstance(BaseResource):
    schema = AnalysisSystemInstanceSchema()
    endpoint = 'analysis_system_instance'

    def __repr__(self):
        return '[AnalysisSystemInstance] {}'.format(self.uuid)

    def __str__(self):
        return self.__repr__()
