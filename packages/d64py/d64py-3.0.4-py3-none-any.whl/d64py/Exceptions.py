#======================================================================
# Exceptions.py
#======================================================================
from d64py.Chain import Chain
from d64py.DirEntry import DirEntry

class GeometryException(BaseException):
    def __init__(self, message):
        super("Track or sector number out of range.")

class InvalidRecordException(BaseException):
    def __init__(self, message):
        super(str, "Invalid or deleted VLIR record requested.")

class PartialChainException(BaseException):
    partialChain: Chain

    def __init__(self, message, partialChain: Chain):
        super().__init__(message)
        self.partialChain = partialChain

    def getPartialChain(self) -> Chain:
        return self.partialChain

class PartialDataException(BaseException):
    """
    Exception type for a text file whose chain contains an invalid track and
    sector or a circular reference. The partial data are contained within
    the exception.
    """
    def __init__(self, message: str, partialData: list):
        super(message)
        self.partialData = partialData

class PartialDirectoryException(BaseException):
    partialDir: list[DirEntry]

    def __init__(self, message, partialDir: list[DirEntry]):
        super().__init__(message)
        self.partialDir = partialDir

    def getPartialDir(self) -> list[DirEntry]:
        return self.partialDir
