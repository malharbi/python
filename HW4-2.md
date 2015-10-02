import os
import fnmatch

filename=input("Enter the file name : ")
filePath=input("Enter the start path : ")

if os.path.exists(filePath) == True:
    for direction, listOFdir, filesL in os.walk(filePath):
        for file in filesL:
            if fnmatch.fnmatch(filename, file) == True:
                openFile=open(os.path.join(direction, file))
                for line in openFile:
                    for word in line.split():
                        if word == "password":
                            print("Theer is a password in..", filename," : ",line)
else:
    print(filePath,"..Not correct")
