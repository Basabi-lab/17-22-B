import unittest
from runner import Runner
from runner import Scanner
from utils.utils import Utils

class TestRunner(unittest.TestCase):
    imgpath = "datasets/testdata/test1.jpg"
    store_amount = 1
    ans = ''.join(["A","B","C","0","3","2","6","8"])
    parts_id = "A001"
    place_id = 0

    def test_runner_process(self):
        runner = Runner()
        runner.process(TestRunner.imgpath, TestRunner.store_amount)
        self.assertTrue(False) # TODO: 暫定的に落としてるが、ちゃんとテスト書く

    def test_main_loop(self):
        runner = Runner()
        runner.main_loop()
        self.assertTrue(False) # TODO: 暫定的に落としてるが、ちゃんとテスト書く

class TestScanner(unittest.TestCase):
    dir_empty  = "datasets/scan_test_dir/empty"
    dir_sample = "datasets/scan_test_dir/sample"
    dir_work   = "datasets/work_test_dir"
    def test_img_detect(self):
        empty  = Scanner(TestScanner.dir_empty, TestScanner.dir_work)
        sample = Scanner(TestScanner.dir_sample, TestScanner.dir_work)
        self.assertTrue(empty.detect() == None)
        self.assertTrue(sample.detect() == True)

    def test_have_imgname(self):
        pass

    def test_get_imgname(self):
        pass

    def test_img_move(self):
        pass

    def test_scan_start(self):
        empty = Scanner(TestScanner.dir_empty, TestScanner.dir_work)

    def test_img_scan(self):
        empty  = Scanner(TestScanner.dir_empty, TestScanner.dir_work)
        sample = Scanner(TestScanner.dir_sample, TestScanner.dir_work)
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

