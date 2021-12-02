


from tkinter import *




def but1():
    print("Button one was pushed")


win = Tk()
f = Frame(win)
b1 = Button(f,text="One")
b2 = Button(f,text="Two")
b3 = Button(f,text="Three")

b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)

lbl1 = Label(win,text="This label is over all buttons")
lbl1.pack()
f.pack()


b1.configure(command=but1,text="Uno")
