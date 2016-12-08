class AnalysisSystemInstance:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return '[AnalysisSystemInstance] {}'.format(self.uuid)

    def __str__(self):
        return self.__repr__()
