from tkinter import*
win=Tk()
win.geometry("600x400+400+200")
Label(win,text="Hello Welcome",font="12",fg="#ea67f0",bg="blue",height="2",width="65").grid()
Button(win,text="Click Me", font="12").grid(column="0",row="100")






win.mainloop()
