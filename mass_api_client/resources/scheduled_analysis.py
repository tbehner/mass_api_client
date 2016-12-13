from mass_api_client.schemas import ScheduledAnalysisSchema
from .base import BaseResource


class ScheduledAnalysis(BaseResource):
    schema = ScheduledAnalysisSchema()

    def get(self, analysis_id):
        return self._get_detail_from_url("scheduled_analysis/{}/".format(analysis_id))