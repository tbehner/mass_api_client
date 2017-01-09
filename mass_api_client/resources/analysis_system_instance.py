from mass_api_client.schemas import AnalysisSystemInstanceSchema
from .base import BaseResource
from .scheduled_analysis import ScheduledAnalysis


class AnalysisSystemInstance(BaseResource):
    schema = AnalysisSystemInstanceSchema()
    endpoint = 'analysis_system_instance'

    def schedule_analysis(self, sample):
        return ScheduledAnalysis.create(self, sample)

    def __repr__(self):
        return '[AnalysisSystemInstance] {}'.format(self.uuid)

    def __str__(self):
        return self.__repr__()
