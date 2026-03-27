from tkinter import*
win=Tk()
win.title("My App")
win.geometry("600x400+400+200")
Label(win,text="Enter your Name:",font="none 15").grid()
Entry(win,bg="yellow").grid()
Button(win,text="click me",font="none 14",height="1").grid()




win.mainloop()
