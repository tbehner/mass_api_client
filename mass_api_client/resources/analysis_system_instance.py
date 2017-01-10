from mass_api_client.schemas import AnalysisSystemInstanceSchema
from .base import BaseResource
from .scheduled_analysis import ScheduledAnalysis


class AnalysisSystemInstance(BaseResource):
    schema = AnalysisSystemInstanceSchema()
    endpoint = 'analysis_system_instance'
    creation_point = endpoint

    @classmethod
    def create(cls, analysis_system):
        return cls._create(analysis_system=analysis_system)

    def schedule_analysis(self, sample):
        return ScheduledAnalysis.create(self.url, sample.url)

    def get_scheduled_analyses(self):
        url = '{}scheduled_analyses/'.format(self.url)
        return ScheduledAnalysis._get_list_from_url(url, append_base_url=False)

    def __repr__(self):
        return '[AnalysisSystemInstance] {}'.format(self.uuid)

    def __str__(self):
        return self.__repr__()
