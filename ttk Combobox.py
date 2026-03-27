from tkinter import*
from tkinter import ttk
win=Tk()
win.geometry("600x400")
win.title("Combo Box")

dic={"padx":10,"pady":20}

lb1=Label(win,text="Item1",font="none 20",**dic)
lb1.grid(column=0,row=0,**dic,sticky=W)

items=["item1","item2","item3","item4"]

itcb=ttk.Combobox(win,width="10",values=items,font="none 20")
itcb.grid(column=1,row=0,**dic,sticky=W)

win.mainloop()
