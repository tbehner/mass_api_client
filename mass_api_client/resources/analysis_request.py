from mass_api_client.schemas import AnalysisRequestSchema
from .base import BaseResource


class AnalysisRequest(BaseResource):
    schema = AnalysisRequestSchema()
    endpoint = 'analysis_request'
