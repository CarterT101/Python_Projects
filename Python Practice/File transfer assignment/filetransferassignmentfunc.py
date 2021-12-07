

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



src = StringVar() #temp variables
dest = StringVar()


def chooseSource(self):
    src=fd.askdirectory()
    self.txtEntry.delete(0,END) #deletes text if necessary
    self.txtEntry.insert(END,src) #inserts text
    return src 


def chooseDest(self):
    dest = fd.askdirectory()
    self.txtEntry1.delete(0,END)
    self.txtEntry1.insert(END,dest)
    return dest 


def fileMove(self):
    secondsinday=24*60*60                   #basic variables necessary for app to work
    pattern = "/*.txt"
    now=time.time()
    before = now - secondsinday
    files = glob.glob(src.get() + pattern, recursive=True) #creates file path
    for i in files:
        try:
            mtime=os.path.getmtime(i)
        except OSError:
            mtime=0
        lastmodifieddate=datetime.datetime.fromtimestamp(mtime)
        lmd=lastmodifieddate.timestamp()
        if lmd < now and lmd > before: #if it is between 24 hours ago and now, it will move the files
            shutil.move(i,dest.get()) 



if __name__ == "__main__":
    pass
