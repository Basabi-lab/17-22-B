import os
class Runner:
    def __init__(self):
        pass

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
