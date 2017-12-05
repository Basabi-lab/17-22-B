import unittest
import numpy as np
import cv2
from read_datasets import Datasets

class DatasetsTest(unittest.TestCase):
    def test_equaly(self):
        data16 = Datasets("16")
        data32 = Datasets("32")
        self.assertTrue(data16 == Datasets("16"))
        self.assertFalse(data16 == data32)

    def test_load_base(self):
        data = Datasets("16")
        target_names = np.array(["0","1","2","3","4","5","6","7","8","9","A","B","C","="])
        target_names_eq = data.target_names == target_names
        target_names_eq = np.where(target_names_eq == True)[0]

        self.assertTrue(len(target_names_eq) == len(target_names))
        self.assertEqual(data.size,   "16")

    def test_load_detail(self):
        data16 = Datasets.load_16()
        data32 = Datasets.load_32()
        self.assertEqual(data16.size, "16")
        self.assertEqual(data32.size, "32")
        self.assertTrue(hasattr(data32, "size"))
        self.assertTrue(hasattr(data32, "target"))
        self.assertTrue(hasattr(data32, "target_names"))
        self.assertTrue(hasattr(data32, "data"))

    def test_load_target_and_data(self):
        target, data = Datasets("16").target, Datasets("16").data
        self.assertTrue(len(target) == 366)
        self.assertTrue(len(data) == 366)

    def test_data(self):
        data = Datasets("32")
        for d,t in zip(data.data,data.target):
            # cv2.imshow(t, d)
            # key = cv2.waitKey(0)
            # cv2.destroyAllWindows()
            pass

if __name__ == "__main__":
    unittest.main()
