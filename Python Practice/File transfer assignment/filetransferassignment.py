

import os               #all necessary modules
from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd
import datetime
import time
import glob
import shutil


class ParentWindow(Frame):
    def __init__(self,master, *args, **kargs):
        Frame.__init__(self)
        
        
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
        

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(450,175)) #making app box
        self.master.title('Move files')

        self.txtEntry = tk.Entry(self.master,width=30,font=("Arial",12),textvariable=src)
        self.txtEntry.grid(row=1,column=2,columnspan=4,padx=10,pady=(20,10))

        self.txtEntry1 = tk.Entry(self.master,width=30,font=("Arial",12),textvariable=dest)
        self.txtEntry1.grid(row=2,column=2,columnspan=4,padx=10,pady=(20,10))

        self.btnSource = tk.Button(self.master,width=15,height=1,text='Choose Source',command=lambda:chooseSource(self))
        self.btnSource.grid(row=1,column=1,padx=10,pady=(20,10))

        self.btnDest = tk.Button(self.master,width=15,height=1,text='Choose Destination',command=lambda:chooseDest(self))
        self.btnDest.grid(row=2,column=1,padx=10,pady=(20,10))

        self.btnMove = tk.Button(self.master,width=15,height=1,text='Move Files',command=lambda:fileMove(self))
        self.btnMove.grid(row=3,column=5,padx=10,pady=(20,10),sticky=SE)




if __name__ == "__main__":
    root = Tk() #connects Tk to root variable for next line to use 
    App = ParentWindow(root)
    root.mainloop #keeps tab open, if this is not here it will pop up and disappear 
