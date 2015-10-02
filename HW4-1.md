import os
import fnmatch
start_path=input("enter the start path :\t")
file_name=input("enter the file name :\t")
if os.path.exists(start_path) == True:
        for direction, listOFdir, filesL in os.walk(start_path, topdown=True):
                for name in fnmatch.filter(filesL, file_name):
                        print( os.path.join(direction, name))
else:
        print("the start path doesn't correct")
