

import os               #all necessary modules
from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd
import datetime
import time
import glob
import shutil

import filetransferassignmentgui
import filetransferassignment






def chooseSource(self):
    self.txtEntry.delete(0,END) #deletes text if necessary
    src=fd.askdirectory()
    self.txtEntry.insert(0,src) #inserts text
    return src 


def chooseDest(self):
    self.txtEntry1.delete(0,END)
    dest = fd.askdirectory()
    self.txtEntry1.insert(0,dest)
    return dest 


def fileMove(self):
    self.src = self.txtEntry.get() #temp variables
    self.dest = self.txtEntry1.get()                   #basic variables necessary for app to work
    pattern = "/*.txt"
    now=datetime.datetime.now()
    before = now - datetime.timedelta(hours=24)
    files = glob.glob(self.src + pattern) #creates file path
    for i in files:
        mtime=os.path.getmtime(i)
        lastmodifieddate=datetime.datetime.fromtimestamp(mtime)
        if lastmodifieddate < now and lastmodifieddate > before: #if it is between 24 hours ago and now, it will move the files
            shutil.move(i,self.dest) 



if __name__ == "__main__":
    pass
