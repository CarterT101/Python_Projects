




import os
import ntpath
import time
import datetime




files = os.listdir('C:\python_test')

now = os.path.dirname('C:\python_test\hello.txt')

sources = "C:\\python_test"
destinations = "C:\\python_test"

for file in files:
    if file.endswith('.txt'):
        timeMod = ntpath.getmtime(os.path.join(sources,file))
        timestamp= datetime.datetime.fromtimestamp(timeMod)
        print(os.path.join(file) + " = " + str(timestamp))



