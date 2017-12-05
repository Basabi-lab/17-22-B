import cv2
import os
import threading
from queue import Queue
import shutil

from joblib import Parallel, delayed

from recog.recog  import Recog
from store.store  import Store
from plot.plot    import Plot
from utils.resize import Resize

class Runner:
    def __init__(self):
        self.recog = Recog("16")
        self.store = Store()
        self.plot  = Plot()

    def process(self, imgpath, amount):
        place_id_list = self.recog.recog(imgpath)
        parts_id = self.store.store(''.join(place_id_list), amount)
        self.plot.plotAt(parts_id)
        self.plot.plot()

class Scanner:
    def __init__(self, scan_dir, work_dir):
        self.scan_dir = scan_dir
        self.work_dir = work_dir
        self.queue = Queue()
        self.scan_start()

    def is_empty(files):
        return files == []

    def detect(self):
        files = os.listdir(self.scan_dir)
        if Scanner.is_empty(files):
            return None
        else:
            return files[0]

    def dump_to_working(self, img, imgname):
        wimgpath = ''.join([self.work_dir, "/", imgname])
        simgpath = ''.join([self.scan_dir, "/", imgname])

        os.remove(simgpath)
        cv2.imwrite(wimgpath, img)

    def have_imgname(self):
        return not self.queue.empty()

    def get_imgname(self):
        return self.queue.get(block=True, timeout=1)

    def scan_start(self):
        threading.Thread(target=self.scan,name="scan_thread",args=())

    def scan(self):
        if self.detect():
            imgname = self.detect()
            img = cv2.imread(''.join([self.scan_dir, "/", imgname]), 0)

            cv2.imshow(imgname, img)
            key = cv2.waitKey(0)
            cv2.destroyAllWindows()

            resized = Resize.resize(img, 500, padding_flg=False)
            self.dump_to_working(resized, imgname)
            self.queue.put(imgname, block=True)
