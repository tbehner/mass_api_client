from mass_api_client.schemas import AnalysisRequestSchema
from .base import BaseResource


class AnalysisRequest(BaseResource):
    schema = AnalysisRequestSchema()

    def get(self, request_id):
        return self._get_detail_from_url("analysis_request/{}/".format(request_id))
