import netCDF4
import numpy as np
from modules import extract
from netCDF4 import Dataset

'''
Input: a List with the paths to all the CSV Files.
Output: a List with the same dimensions containing the average for each array
This Function averages sums each index within the array and returns the average
within each position.
'''
# Calculates the mean for CSVs in a path list 
def calcMean(pathList):
    length = len(pathList)
    #Create list of numpy arrays from file path
    for i in range(0,length): 
        pathList[i] = np.genfromtxt(pathList[i], delimiter =",")
    return np.mean(np.array(pathList), axis = 0) 


# Calculates the x,y position based on hour
def calcMeanNC(z, zVarName):
    mean =  np.mean(z,axis =0)
    return(mean) 

