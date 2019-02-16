#OS Module

import os

#To find the current directory
currentDir = os.getcwd()
print(currentDir)

#To creat new directory
os.mkdir('NuDir')


import time
time.sleep(2)

os.rename('NuDir','NuDir2')

time.sleep(2)

os.rmdir('NuDir2') #To remove directory


