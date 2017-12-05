import numpy as np
import unittest

from utils.utils import Utils

from recog.recog import DataFormat

data1 = np.array(
        [[1.,0.,0.,0.],
         [0.,1.,0.,0.],
         [0.,0.,1.,0.],
         [0.,0.,0.,1.]]
    )
data2 = np.array(
        [[1.,0.,0.,1.],
         [0.,1.,0.,0.],
         [1.,1.,1.,1.],
         [1.,1.,0.,1.]]
    )

class TestDataFormat(unittest.TestCase):
    def test_framing(self):
        ans1 = np.array([2.,0.,0.,2.])
        ans2 = np.array([2.,1.,4.,3.])

        self.assertTrue(Utils.nparray_eq(DataFormat.framing(data1, 2), ans1))
        self.assertTrue(Utils.nparray_eq(DataFormat.framing(data2, 2), ans2))
    def test_column(self):
        ans1 = np.array([1.,1.,1.,1.])
        ans2 = np.array([3.,3.,1.,3.])

        self.assertTrue(Utils.nparray_eq(DataFormat.column(data1), ans1))
        self.assertTrue(Utils.nparray_eq(DataFormat.column(data2), ans2))

    def test_row(self):
        ans1 = np.array([1.,1.,1.,1.])
        ans2 = np.array([2.,1.,4.,3.])

        self.assertTrue(Utils.nparray_eq(DataFormat.row(data1), ans1))
        self.assertTrue(Utils.nparray_eq(DataFormat.row(data2), ans2))

    def test_step_column(self):
        ans1 = np.array([2., 2.])
        ans2 = np.array([4., 6.])

        self.assertTrue(Utils.nparray_eq(DataFormat.step_column(data1, 2), ans1))
        self.assertTrue(Utils.nparray_eq(DataFormat.step_column(data2, 2), ans2))

    def test_step_row(self):
        ans1 = np.array([2., 2.])
        ans2 = np.array([6., 4.])

        self.assertTrue(Utils.nparray_eq(DataFormat.step_row(data1, 2), ans1))
        self.assertTrue(Utils.nparray_eq(DataFormat.step_row(data2, 2), ans2))

    def test_continuous_column(self):
        ans1 = np.array([2., 2.])
        ans2 = np.array([6., 4.])

        self.assertTrue(Utils.nparray_eq(DataFormat.continuous_column(data1, 2), ans1))
        self.assertTrue(Utils.nparray_eq(DataFormat.continuous_column(data2, 2), ans2))

    def test_continuous_row(self):
        ans1 = np.array([2., 2.])
        ans2 = np.array([3., 7.])

        self.assertTrue(Utils.nparray_eq(DataFormat.continuous_row(data1, 2), ans1))
        self.assertTrue(Utils.nparray_eq(DataFormat.continuous_row(data2, 2), ans2))

if __name__ == '__main__':
    unittest.main()
