from tkinter import*
win=Tk()
win.title('Label')
win.geometry('600x400+500+200')
win.configure(bg="White")
win.columnconfigure(0,weight=2)
win.columnconfigure(1,weight=1)

Label(win,text="Hello Welcome",font="none 20").grid(row=0,column=0,sticky=W)





win.mainloop()
