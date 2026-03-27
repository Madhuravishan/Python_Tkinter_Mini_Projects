from tkinter import*
win=Tk()
win.title("Simple Calculator")
win.geometry("600x400")


lbl1=Label(win,text="Enter first Number:",font="none 20")
lbl1.grid(row=0,column=0,sticky=W,padx=10,pady=20)

lbl2=Label(win,text="Enter Second Number:",font="none 20")
lbl2.grid(row=1,column=0,sticky=W,padx=10,pady=20)

etr1=Entry(win,font="none 20",width=15)
etr1.grid(row=0,column=1,sticky=W,padx=10,pady=20)

etr2=Entry(win,font="none 20",width=15)
etr2.grid(row=1,column=1,sticky=W,padx=10,pady=20)


win.mainloop()
