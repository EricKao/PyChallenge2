# This program implement a function that list all files in the given folder
#
# Created by Eric

import os

def FindDirContents(Dir):
    for Path in os.listdir(Dir):
        DirPath = os.path.join(Dir, Path)
        if os.path.isdir(DirPath):
            FindDirContents(DirPath)
        else:
            print DirPath

def main():
    # Get the all files inside the folder
    FindDirContents(r'C:\Users\eric_kao\Desktop\Eclipse')

if __name__ == "__main__":
    main()
