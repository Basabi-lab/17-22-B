import unittest

from tests.test_runner import TestRunner
from tests.test_runner import TestScanner
from tests.test_runner import TestQueue

from tests.test_store                  import TestStore
from tests.test_plot                   import TestPlot
from tests.test_recog.test_recog       import TestRecog
from tests.test_recog.test_data_format import TestDataFormat
from tests.test_utils.test_resize      import TestResize

if __name__ == '__main__':
    unittest.main()
