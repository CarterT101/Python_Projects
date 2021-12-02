


from tkinter import *


win = Tk()


b1 = Button(win, text="One")
b2 = Button(win, text="Two")
b3 = Button(win, text="Three")
b4 = Button(win,text="Four")


b1.grid(row=0,column=0)
b2.grid(row=1,column=1)
b3.grid(row=2,column=2)
b4.grid(row=3,column=3)

lbl1 = Label(win,text="This is a label")
lbl1.grid(row=1,column=0)





#b1.pack(side=LEFT, padx=10)
#b2.pack(side=TOP, padx=10)
#b3.pack(side=BOTTOM, padx=10)
#b4.pack(side=RIGHT, padx=10)
