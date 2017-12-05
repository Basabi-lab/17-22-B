import numpy as np
import pandas as pd
import unittest

from store.store import Store

class TestStore(unittest.TestCase):

    def tests_store(self):
        parts = np.array(pd.read_csv("datasets/parts.csv", header=None, sep=","))
        samples = parts[np.random.randint(0,parts.shape[0],20)]
        # print(samples)
        store = Store()
        for sample in samples:
            place_id = store.store(sample[0], np.random.rand(1,10))
            part_id, count = store.lookup(place_id)
            # if count > 0:
            #     print("Test case part {}: Success!", sample)
            # else:
            #     print("Test case part {}: Failure!", sample)
            # self.assertTrue(count > 0)
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
