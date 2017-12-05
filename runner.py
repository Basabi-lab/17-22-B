import os

from recog.recog import Recog
from store.store import Store
from plot.plot   import Plot

class Runner:
    def __init__(self):
        self.amount = 1
        self.recog = Recog("16")
        self.store = Store()
        self.plot  = Plot()

    def process(self, imgpath):
        place_id_list = self.recog.recog(imgpath)
        parts_id = self.store.store(''.join(place_id_list), self.amount)
        self.plot.plotAt(parts_id)

class Scanner:
    def __init__(self, scan_dir):
        self.scan_dir = scan_dir

    def is_empty(files):
        return files == []

    def detect(self):
        files = os.listdir(self.scan_dir)
        if not Scanner.is_empty(files):
            return files[0]
        else:
            return None

    def scan(self):
        pass

class Queue:
    def __init__(self):
        pass
