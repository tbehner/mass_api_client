from mass_api_client.schemas import AnalysisSystemSchema
from .analysis_system_instance import AnalysisSystemInstance
from .base import BaseResource


class AnalysisSystem(BaseResource):
    schema = AnalysisSystemSchema()
    endpoint = 'analysis_system'
    creation_point = endpoint

    @classmethod
    def create(cls, identifier_name, verbose_name, tag_filter_expression=''):
        return cls._create(identifier_name=identifier_name, verbose_name=verbose_name, tag_filter_expression=tag_filter_expression)

    def create_analysis_system_instance(self):
        return AnalysisSystemInstance.create(analysis_system=self)

    def __repr__(self):
        return '[AnalysisSystem] {}'.format(self.identifier_name)

    def __str__(self):
        return self.__repr__()
