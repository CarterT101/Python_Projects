
import datetime 
import time
import glob
import shutil
import os

secondsinday = 24*60*60

source = '/Users/hoove/Desktop/foldera/' #set where source of files are

destination = '/Users/hoove/Desktop/folderb/' #set destination path to folderb

pattern = "\*.txt" #finds specific extension
files = glob.glob(source + pattern) #returns path names that match pathname
now=time.time() #gets time 
before = now - secondsinday #sets it 24 hours back 

def fileMove():
    for i in files:
        try:
            mtime=os.path.getmtime(i) #used to get last modification of specific path
        except OSError:
            mtime=0
        lastmodifieddate = datetime.datetime.fromtimestamp(mtime) #sets last modified time in specific data type
        lmd = lastmodifieddate.timestamp() 
        if lmd < now and lmd > before: #makes sure it has been modified within 24 hours so it can move it
            print(lastmodifieddate)
            file_name = os.path.basename(i) #gathers name of file
            shutil.move(i,destination + file_name) #moves file to destination
            print('Moved:',i)


fileMove()


    
