
import datetime 
import time
import glob
import shutil
import os


secondsinday = 24*60*60

source = '/Users/hoove/Desktop/foldera/' #set where source of files are

destination = '/Users/hoove/Desktop/folderb/' #set destination path to folderb

pattern = "\*.txt"
files = glob.glob(source + pattern)
now=time.time()
before = now - secondsinday




def fileMove():
    for i in files:
        try:
            mtime=os.path.getmtime(i)
        except OSError:
            mtime=0
        lastmodifieddate = datetime.datetime.fromtimestamp(mtime)
        lmd = lastmodifieddate.timestamp()
        if lmd < now and lmd > before:
            print(lastmodifieddate)
            file_name = os.path.basename(i)
            shutil.move(i,destination + file_name)
            print('Moved:',i)


fileMove()


    
