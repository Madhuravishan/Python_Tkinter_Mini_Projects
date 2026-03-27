from tkinter import*
import tkinter
def cb():
    c1.deselect()
    c2.deselect()
    print(check1+check2)
top=Tk()
check1=1
check2=2
c1=Checkbutton(top,text="Music",variable=check1,onvalue=1,offvalue=0,height=5,width=20)
c2=Checkbutton(top,text="Video",variable=check2,onvalue=1,offvalue=0,height=5,width=20)

btn=Button(top,text="clear",command=cb)

btn.pack()
c1.pack()
c2.pack()

top.mainloop()
