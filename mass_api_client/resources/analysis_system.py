class AnalysisSystem:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return '[AnalysisSystem] {}'.format(self.identifier_name)

    def __str__(self):
        return self.__repr__()
