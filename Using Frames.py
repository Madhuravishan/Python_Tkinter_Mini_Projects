from tkinter import*

win=Tk()
win.geometry("500x400+500+300")
win.title("Using Frames")
#add dictionary for padx pady
pad={"padx":10,"pady":10}
#create frames
frame1=LabelFrame(win,text="Input")
frame1.pack(side=TOP,expand="yes",fill="both")
frame2=LabelFrame(win,text="Output")
frame2.pack(side=BOTTOM,expand="yes",fill="both")
#add labels
lbln=Label(frame1,text="Enter name:",font="none 15",**pad)#** forcall to dictionary 
lbln.grid(row=0,column=0,sticky=W)
lbl1s=Label(frame1,text="Subject 1:",font="none 15",**pad)
lbl1s.grid(row=1,column=0,sticky=W)
lbl2s=Label(frame1,text="Subject 2:",font="none 15",**pad)
lbl2s.grid(row=2,column=0,sticky=W)
#add entry boxes
entrn=Entry(frame1,font="none 13",width=10)
entrn.grid(row=0,column=1,sticky=W,**pad)
entr1s=Entry(frame1,font="none 13",width=10)
entr1s.grid(row=1,column=1,sticky=W,**pad)
entr2s=Entry(frame1,font="none 13",width=10)
entr2s.grid(row=2,column=1,sticky=W,**pad)


win.mainloop()
