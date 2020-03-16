from os import path

# Checks if path exists and returns true, otherwise returns false
def checkPath(fPath):
    if path.exists(fPath):
        return True
    return False
