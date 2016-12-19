from mass_api_client.schemas import ReportSchema
from .base import BaseResource


class Report(BaseResource):
    REPORT_STATUS_CODE_OK = 0
    REPORT_STATUS_CODE_FAILURE = 1

    REPORT_STATUS_CODES = [REPORT_STATUS_CODE_OK, REPORT_STATUS_CODE_FAILURE]

    schema = ReportSchema()
    endpoint = 'report'

    def __repr__(self):
        return '[Report] {} on {}'.format(self.sample, self.analysis_system)

    def __str__(self):
        return self.__repr__()
