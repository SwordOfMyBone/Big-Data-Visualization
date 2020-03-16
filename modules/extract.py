import netCDF4
from netCDF4 import Dataset


def getVarKeys(keyArr):
    # Gets a dict of all of the keys  
    keys = keyArr.variables.keys()
    return(keys)

def printKeys(keyArr):
    counter = 0 
    for key in keyArr:
        print(counter, ". ", key, sep="", end=",\n")
        counter += 1

#returns a 2d array containing the hour, Lon and Lat variables.
def extractConst(path): 
    lat = keyArr['lat'] 
    lon = data.variables['lon']
    hour = data.variables['hour']
    return({"hours" : hour,"lat": lat,"lon": lon})


