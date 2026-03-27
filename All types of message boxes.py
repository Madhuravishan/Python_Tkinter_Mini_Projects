from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("300x200")

messagebox.showinfo("Show Information","This is my first Information box")

messagebox.showwarning("Warning","This is my first Warning box")

messagebox.showerror("Error","This is my first Error box")

messagebox.askquestion("question","This is my first question box")

messagebox.askokcancel("OkCancel","This is my first OkCancel box")

messagebox.askyesno("YesNo","This is my first YesNo box")

messagebox.askretrycancel("RetryCancel","This is my first RetryCancel box")



root.mainloop()
