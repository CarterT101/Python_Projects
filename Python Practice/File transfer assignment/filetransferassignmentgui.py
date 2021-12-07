

import os               #all necessary modules
from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd
import datetime
import time
import glob
import shutil

import filetransferassignment
import filetransferassignmentfunc



def load_gui(self):
    
        self.txtEntry = tk.Entry(self.master,width=30,font=("Arial",12),textvariable=src)
        self.txtEntry.grid(row=1,column=2,columnspan=4,padx=10,pady=(20,10))

        self.txtEntry1 = tk.Entry(self.master,width=30,font=("Arial",12),textvariable=dest)
        self.txtEntry1.grid(row=2,column=2,columnspan=4,padx=10,pady=(20,10))

        self.btnSource = tk.Button(self.master,width=15,height=1,text='Choose Source',command=lambda:filetransferassignmentfunc.chooseSource(self))
        self.btnSource.grid(row=1,column=1,padx=10,pady=(20,10))

        self.btnDest = tk.Button(self.master,width=15,height=1,text='Choose Destination',command=lambda:filetransferassignmentfunc.chooseDest(self))
        self.btnDest.grid(row=2,column=1,padx=10,pady=(20,10))

        self.btnMove = tk.Button(self.master,width=15,height=1,text='Move Files',command=lambda:filetransferassignmentfunc.fileMove(self))
        self.btnMove.grid(row=3,column=5,padx=10,pady=(20,10),sticky=SE)

    


if __name__ == "__main__":
    pass
