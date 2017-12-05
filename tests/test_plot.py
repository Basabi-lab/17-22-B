import numpy as np
import pandas as pd
import unittest

from plot.plot import Plot

class TestPlot(unittest.TestCase):
    def test_plot(self):
        shelf = np.array(pd.read_csv("datasets/shelf.csv", header=None))
        samples = np.random.randint(0,shelf.shape[0],20)
        # print(samples)
        plot = Plot()
        for sample in samples:
            plot.plotAt(sample)
            plot.plot()
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
