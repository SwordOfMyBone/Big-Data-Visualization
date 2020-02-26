import netCDF4
import numpy as np

'''
Input: a List with the paths to all the lists.
Output: a List with the same dimensions containing the average for each array
This Function averages sums each index within the array and returns the average
within each position.
'''
def calcMean(pathList):
    length = len(pathList)
    #Create list of numpy arrays from file path
    for i in range(0,length): 
        pathList[i] = np.genfromtxt(pathList[i], delimiter =",")
    return np.mean(np.array(pathList), axis = 0) 



