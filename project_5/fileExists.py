import os

#create decorator function called Exists
def Exists(oldFunc):
    def inside(filename):
        if (os.path.exists(filename)):
            oldFunc(filename)
        else:
            print("The File does not exist.")
    return inside

@Exists
def outputLine(inFile):
    with open(inFile) as f:
        print(f.readlines())

outputLine("fileExists.py")
outputLine("abc.py")
