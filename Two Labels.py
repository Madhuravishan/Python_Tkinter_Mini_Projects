from tkinter import*
win=Tk()
win.title('Two Labels')
win.geometry('800x400+100+200')
win.title("My App")

Label(win,text="This is my Main Window",font="none 20")\
                     .grid(row=10,column=10,sticky=E)
Label(win,text="This is second label",font="none 20")\
                     .grid(row=20,column=10,sticky=W)





win.mainloop()

