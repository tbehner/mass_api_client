from mass_api_client.schemas import ScheduledAnalysisSchema
from .base import BaseResource
from .report import Report


class ScheduledAnalysis(BaseResource):
    schema = ScheduledAnalysisSchema()
    endpoint = 'scheduled_analysis'

    def create_report(self, json_report_objects={}, raw_report_objects={}, tags=[]):
        return Report.create(self, json_report_objects, raw_report_objects)