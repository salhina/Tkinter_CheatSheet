#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
#Initialite main windows with title and size top	
top = Tk()
top.title("Hollo GUI")
top.minsize(200,30)

def Sclcallback(a):
    L.configure(text="The Angle is : "+a+"°")
    
# •Label():
Label(top,text="•Label()").pack(anchor=W)
L = Label(top, text="Hello!")
L.pack()
    
# •Scale()
Label(top,text="•Scale()").pack(anchor=W)
S = Scale(top,
    command = Sclcallback,
    to      = 180,    from_=10,
    orient  = HORIZONTAL,
    length  = 400,
    label   = 'Angle'     )
S.pack(anchor = CENTER)

# •Button()
Label(top,text="•Button()").pack(anchor=W)
def BtCallBack():    #B.config(state=DISABLED) #B.config(state=ACTIVE)
    L.configure(text="The button was Clicked !!")
B = Button(top, text="Click!!"	, command=BtCallBack).pack() 
Bxx = Button(top, text="Exit !!"	, command=top.quit  ).pack()

# •Entry()
Label(top,text="•Entry()").pack(anchor=W)
def ECallBack():  L.configure(text=E.get())
E  = Entry (top, bd = 2 , width= 25 )
EnB= Button(top,text="EntryButton",command= ECallBack )
E  .pack()
E  .focus_set()
EnB.pack()

# •Checkbox()
Label(top,text="•Checkbox()").pack(anchor=W)
def CbCallBack():      L.configure(text=CbVar.get())
CbVar= IntVar()
Cb   = Checkbutton(top, text="Option_1"    ,variable=CbVar    ).pack()
EnB  = Button     (top, text="ChkBoxButton",command=CbCallBack).pack()

# run Tk event loop
top.mainloop()
