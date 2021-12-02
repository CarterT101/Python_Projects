


from tkinter import *

win=Tk()

lb= Listbox(win,height=3)
lb.pack()
lb.insert(END, "first entry")
lb.insert(END, "second entry")
lb.insert(END, "third entry")
lb.insert(END, "fourth entry")

sb = Scrollbar(win, orient=VERTICAL)
sb.pack(side=LEFT,fill=Y) #scrollbar


sb.configure(command=lb.yview) #lines of code to make sure the listbox and scrollbar
lb.configure(yscrollcommand=sb.set) #recognize each other

lb.curselection() #return the selected item for you, returns a tuple of items selected
