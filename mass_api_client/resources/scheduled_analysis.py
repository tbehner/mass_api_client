from mass_api_client.schemas import ScheduledAnalysisSchema
from .base import BaseResource


class ScheduledAnalysis(BaseResource):
    schema = ScheduledAnalysisSchema()
    endpoint = 'scheduled_analysis'
