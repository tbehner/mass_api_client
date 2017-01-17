from mass_api_client.schemas import ScheduledAnalysisSchema
from .base import BaseResource
from .report import Report


class ScheduledAnalysis(BaseResource):
    schema = ScheduledAnalysisSchema()
    endpoint = 'scheduled_analysis'
    creation_point = endpoint

    @classmethod
    def create(cls, analysis_system_instance, sample):
        return cls._create(analysis_system_instance=analysis_system_instance.url, sample=sample.url)

    def create_report(self, json_report_objects=None, raw_report_objects=None, tags=None):
        return Report.create(self, json_report_objects=json_report_objects, raw_report_objects=raw_report_objects, tags=tags)
