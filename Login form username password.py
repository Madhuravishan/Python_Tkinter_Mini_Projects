from tkinter import*
from tkinter import ttk

win=Tk()
win.title("Login Form")
win.geometry("350x320")

fields={}

fields["username_label"]=ttk.Label(text="Username:")
fields["username"]=ttk.Entry()

fields["password_label"]=ttk.Label(text="Password:")
fields["password"]=ttk.Entry(show="*")

fields["username_label2"]=ttk.Label(text="Username 2:")
fields["username2"]=ttk.Entry()

fields["password_label2"]=ttk.Label(text="Password 2:")
fields["password2"]=ttk.Entry(show="*")

for field in fields.values():
    field.pack(anchor=W,padx=10,pady=5,fill=X)

Button(text="Login").pack(anchor=W,padx=10,pady=5)







win.mainloop()
