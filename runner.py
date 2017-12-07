import cv2
import os
import threading
from queue import Queue
from time import sleep

from recog.recog  import Recog
from store.store  import Store
from plot.plot    import Plot
from utils.resize import Resize

class Runner:
    def __init__(self, scan_dir, work_dir):
        self.recog = Recog.recog16()
        self.store = Store()
        self.plot  = Plot()
        self.work_dir = work_dir
        self.scanner = Scanner(scan_dir, work_dir)
        self.main_process()

    def process(self, imgpath, amount):
        place_id = ''.join(self.recog.recog(imgpath, box_view=True))
        print(place_id)
        parts_id = self.store.store(place_id, amount)
        self.plot.plotAt(parts_id)
        self.plot.plot()

    def get_imgpath(self, imgpath):
        return ''.join([self.work_dir, "/", imgpath])

    def main_process(self):
        while True:
            if self.scanner.have_imgname:
                imgname = self.scanner.get_imgname()
                print("new image load: ", imgname)
                self.process(self.get_imgpath(imgname), 1)
            sleep(1)

class Scanner:
    def __init__(self, scan_dir, work_dir):
        self.scan_dir = scan_dir
        self.work_dir = work_dir
        self.queue = Queue()
        self.scan_start()

    def detect(self):
        files = os.listdir(self.scan_dir)
        if files == []:
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
        return self.queue.get(block=True)

    def scan_start(self):
        scan_th = threading.Thread(target=self.scan_loop,name="scan_thread",args=())
        scan_th.setDaemon(True)
        scan_th.start()

    def scan_loop(self):
        while True:
            self.scan()
            sleep(1)

    def scan(self):
        if self.detect():
            print("detect")
            imgname = self.detect()
            img = cv2.imread(''.join([self.scan_dir, "/", imgname]), 0)

            resized = Resize.resize(img, 500, padding_flg=False)
            # resized = img
            self.dump_to_working(resized, imgname)
            self.queue.put(imgname, block=True)

if __name__ == '__main__':
    # runner = Runner("datasets/scan_test_dir/sample", "datasets/work_test_dir")
    runner = Runner("datasets/scan_test_dir/android/内蔵ストレージ/DCIM/Camera", "datasets/work_test_dir")
