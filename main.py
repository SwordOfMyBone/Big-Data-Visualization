import sys
from modules import ui 
from modules import helper
from os.path import abspath


if __name__ == '__main__':
    # exit if one argument is passed to CLI
    if len(sys.argv) <= 1:
        print("ERROR: Please pass a file path")
        sys.exit()
    
    # Check if path is valid
    else:
        for i in range(1,len(sys.argv)):
            current = sys.argv[i]
            if helper.checkPath(current):
                sys.argv[i] = abspath(current)
                continue
            else:
               sys.exit()
    ui.start(sys.argv[1:])
