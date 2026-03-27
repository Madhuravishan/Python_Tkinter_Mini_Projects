from tkinter import*

win=Tk()
win.geometry("580x400")
win.resizable(0,0)
win.title("Using Frames")

arng={"padx":10,"pady":10}

mframe=Frame(win, bd=8, width=580, height=380, bg="red", relief=RIDGE)
mframe.grid()

lframe=Frame(mframe, width=470, height=370, relief=RIDGE,)
lframe.grid(column=0,row=0)

rframe=Frame(mframe, bd=5, width=100, height=375, relief=RIDGE)
rframe.grid(column=1,row=0)

ltframe=Frame(lframe, bd=5, width=460, height=270, relief=RIDGE,bg="cadet blue")
ltframe.grid(column=0,row=0)

lbframe=Frame(lframe, bd=5, width=460, height=100, relief=RIDGE, bg="#459945")
lbframe.grid(column=0,row=0)


lbframe.grid(column=0,row=1)




win.mainloop()
