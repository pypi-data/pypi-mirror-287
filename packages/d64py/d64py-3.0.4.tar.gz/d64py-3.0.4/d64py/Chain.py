#======================================================================
# Chain.py
#======================================================================
import d64py.TrackSector as TrackSector

class Chain:
    sectors: list[TrackSector]

    def __init__(self, sectors=[]):
        self.sectors = sectors

    def size(self):
        return len(self.sectors)
