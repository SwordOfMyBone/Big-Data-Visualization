
import unittest
import "../calc"
import numpy as np
import glob

class testCalc(unittest.TestCase):

    def test_calcMean(self):
        pathList = glob.glob("meanArr*.csv")
        calcMean = calc.calcMean(pathList)

        #Check if the final array is equal to expected values
        val = np.array([[3.5,5,6],
              [2,6.5,28.5],
              [67.5,48.5,67.5]])

        np.testing.assert_array_almost_equal(val,calcMean)



if __name__ == '__main__':
    unittest.main()
