import unittest
from pyportfolio.statistics import variance
import pandas as pd


class MyTestCase(unittest.TestCase):
    def test_variance(self):
        x=pd.DataFrame([1,2,3,4,5])
        test_output=variance.variance(x)
        expected_out=2.0
        self.assertEqual(expected_out, test_output)

if __name__ == '__main__':
    unittest.main()
