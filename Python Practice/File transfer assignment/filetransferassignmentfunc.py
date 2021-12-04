

import os               #all necessary modules
from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd
import datetime
import time
import glob
import shutil


import filetransferassignment
import filetransferassignmentgui


secondsinday=24*60*60       #basic variables necessary for app to work
pattern = "\.txt"
now=time.time()
before = now - secondsinday
        
        
src = StringVar()
dest = StringVar()


def chooseSource(self):
    src=fd.askdirectory()
    self.txtEntry.delete(0,END)
    self.txtEntry.insert(END,src)
    return src #not sure if i need this

def chooseDest(self):
    dest = fd.askdirectory()
    self.txtEntry1.delete(0,END)
    self.txtEntry1.insert(END,dest)
    return dest #not sure if i need this

def fileMove(self):
    files=glob.glob(src.get()+pattern)
    for i in files:
        try:
            mtime=os.path.getmtime(i)
        except OSError:
            mtime=0
        lastmodifieddate=datetime.datetime.fromtimestamp(mtime)
        lmd=lastmodifieddate.timestamp()
        if lmd < now and lmd > before:
            file_name=os.path.basename(i)
            shutil.move(i,dest.get() + file_name)




                    
if __name__ == "__main__":
    pass
