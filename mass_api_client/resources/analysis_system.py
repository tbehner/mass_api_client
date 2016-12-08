from mass_api_client.schemas import AnalysisSystemSchema
from .base import BaseResource


class AnalysisSystem(BaseResource):
    schema = AnalysisSystemSchema()

    def __repr__(self):
        return '[AnalysisSystem] {}'.format(self.identifier_name)

    def __str__(self):
        return self.__repr__()
