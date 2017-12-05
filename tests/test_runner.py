import unittest
from runner import Runner
from runner import Scanner
from runner import Queue
from utils.utils import Utils

class TestRunner(unittest.TestCase):
    imgpath = "datasets/testdata/test1.jpg"
    ans = ''.join(["A","B","C","0","3","2","6","8"])
    parts_id = "A001"
    place_id = 0

    def test_runner_process(self):
        runner = Runner()
        runner.process()
        self.assertTrue(runner == runner)
        self.assertFalse(runner == Runner())

class TestScanner(unittest.TestCase):
    dir_empty  = "datasets/scan_test_dir/empty"
    dir_sample = "datasets/scan_test_dir/sample"
    def test_img_detect(self):
        empty  = Scanner(TestScanner.dir_empty)
        sample = Scanner(TestScanner.dir_sample)
        self.assertTrue(empty.detect() == None)
        self.assertTrue(sample.detect() == "1")
        # TODO: scan_dir_smapleにファイル2を追加
        self.assertTrue(sample.detect() == "2")

    def have_imgname(self):
        pass

    def get_imgname(self):
        pass

    def test_img_move(self):
        pass

    def test_img_scan(self):
        empty  = Scanner(TestScanner.dir_empty)
        sample = Scanner(TestScanner.dir_sample)
        empty.scan()
        sample.scan()

class TestQueue(unittest.TestCase):
    in_data = "ABC"
    def test_en_de_queue(self):

        queue.dequeue(TestQueue.in_data)
        data = queue.enqueue()

        self.assertTrue(data == TestQueue.in_data)

    def test_now_first(self):
        queue = Queue()

        queue.dequeue(TestQueue.in_data)
        self.assertTrue(queue.now() == TestQueue.in_data)

    def test_conflict(self):
        queue = Queue()
        self.assertTrue(queue.is_using == False)
        # Pararel {
        #     for _ in range(100):
        #         queue.enqueue("10")
        # }
        # self.assertTrue(queue.is_using == True)

    # TODO: Queueの構想
    # if flg == 0 and queue.now():
    #     queue.dequeue()

