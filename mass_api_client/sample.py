class Sample:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return '[{}] {}'.format(str(self.__class__.__name__), str(self.id))

    def __str__(self):
        return self.__repr__()


class DomainSample(Sample):
    pass


class IPSample(Sample):
    pass


class FileSample(Sample):
    pass


class ExecutableBinarySample(FileSample):
    pass
