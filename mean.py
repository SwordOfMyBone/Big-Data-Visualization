import glob
import calc
import numpy as np

def main():
    pathList = glob.glob("24Hour/24HR_CBE_*.csv")
    meanArr = calc.calcMean(pathList)
    return meanArr

print(main())
normal = np.genfromtxt('24Hour/24HR_CBE_01.csv', delimiter = ",")
print("----------------------------")
print(normal)
