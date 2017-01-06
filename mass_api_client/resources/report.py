from mass_api_client.schemas import ReportSchema
from .base import BaseResource


class Report(BaseResource):
    REPORT_STATUS_CODE_OK = 0
    REPORT_STATUS_CODE_FAILURE = 1

    REPORT_STATUS_CODES = [REPORT_STATUS_CODE_OK, REPORT_STATUS_CODE_FAILURE]

    schema = ReportSchema()
    endpoint = 'report'
    creation_point = 'scheduled_analysis/{scheduled_analysis}/submit_report/'

    def __repr__(self):
        return '[Report] {} on {}'.format(self.sample, self.analysis_system)

    def __str__(self):
        return self.__repr__()

    @classmethod
    def create(cls, scheduled_analysis, json_report_objects={}, raw_report_objects={}):
        url = cls.creation_point.format(scheduled_analysis=scheduled_analysis.id)
        return cls._create(url=url, additional_json_files=json_report_objects, additional_binary_files=raw_report_objects, tags=['test'])
