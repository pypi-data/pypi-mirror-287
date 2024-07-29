class DiminiError(Exception):
    pass


class UnknownDependency(DiminiError):
    pass


class InvalidDependency(DiminiError):
    pass


class InvalidOperation(DiminiError):
    pass
