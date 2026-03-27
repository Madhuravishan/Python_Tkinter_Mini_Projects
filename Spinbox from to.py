from tkinter import*
win=Tk()
win.title("Bill")
win.geometry("325x100")
win.resizable(0,0)
dic={"padx":10,"pady":20}

lb1=Label(win,text="Age:",font="none 25",**dic)
lb1.grid(row=0,column=0,sticky=W)

sp1box=Spinbox(win,font="none 25",width="10",from_=16,to=25)
sp1box.grid(row=0,column=1,sticky=W)


win.mainloop()
