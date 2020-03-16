from modules import extract
from modules.calc import calcMeanNC
from modules.visualization import createContMap

# Function to decide on to deal with .nc or .fig
def start(path):
    # If user passes a single .nc file
    if(len(path) == 1):
        # Check that it is a .nc file
        path = path[0]
        if(path[-3:] == ".nc"):
            promptNc(path)
        else:
            print("ERROR: If one file is passed it must be of type .nc")
            exit()

# Handle .nc files to create a plot
def promptNc(path):
    # Prompt the user to pick a variable to use as the Z-axis
    print("Please select the index of the variable to plot")
    varArr = extract.getVarKeys(path)
    extract.printKeys(varArr)
    index = int(input())
    # store Z-variable based on user input
    zVarName = list(varArr)[index]
    mean = calcMeanNC(path, zVarName) 
    constDict = extract.extractConst(keyArr)
    createContMap(constDict['lon'],constDict['lat'],mean,zVarName)
