import numpy as np
import unittest
import cv2

from utils.utils import Resize
from utils.utils import Utils
from utils.read_datasets import Datasets

class TestResize(unittest.TestCase):
    img_to_padding  = np.array([[255,255], [255,0], [0,255], [0,0]])
    padding_ans     = np.array([[0,255,255,0], [0,255,0,0], [0,0,255,0], [0,0,0,0]])
    size = 16
    def test_resize(self):
        data = Datasets.load_32()
        # cv2.imshow("before", data.data[0])
        # key = cv2.waitKey(0)
        # cv2.destroyAllWindows()

        ans = Resize.resize(data.data[0], TestResize.size)
        # cv2.imshow("after", data.data[0])
        # key = cv2.waitKey(0)
        # cv2.destroyAllWindows()

        self.assertTrue(True)

    def test_padding(self):
        self.assertTrue(Utils.nparray_eq(Resize.padding(TestResize.img_to_padding, 4), TestResize.padding_ans))
