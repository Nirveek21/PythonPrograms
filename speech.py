import pyttsx3
from datetime import datetime
from  tkinter import *
window = Tk() # instantiate a window instance
window.geometry('800x400')
window.title("SPEECH TEST")
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-10)
s = StringVar()
def spch():
    
    from datetime import datetime
    t=datetime.today().strftime("%I")
    t1=datetime.today().strftime("%p")
    t=int(t)
    if(t1=='AM'):
        if(int(t)>=5&int(t)<=12):
            engine.say('Meow Meow Nigga , Good Morning ')
    else:
        engine.say(' GOOD EVENING Mah niggar')  
    engine.runAndWait()
def op(x):
    try:
        if x=='+':
            s.set(float(box.get())+float(box1.get()))
            engine.say(box.get() + 'PLUS' + box1.get() + 'EQUALS')
            engine.say(float(box.get())+float(box1.get()))
        elif x=='-':
            s.set(float(box.get())-float(box1.get()))
            engine.say(box.get() + 'MINUS' + box1.get() + 'EQUALS')
            engine.say(float(box.get())-float(box1.get()))
        elif x=='*':
            s.set(float(box.get())*float(box1.get()))
            engine.say(box.get() + 'MULTIPLIED BY' + box1.get() + 'EQUALS')
            engine.say(float(box.get())*float(box1.get()))
        elif x=='/':
            s.set(float(box.get())/float(box1.get()))
            engine.say(box.get() + 'DIVIDED BY' + box1.get() + 'EQUALS')
            engine.say(float(box.get())/float(box1.get()))
    except:
        s.set('Error')   
    engine.runAndWait() 
box = Entry(window)
box.grid(row=0,column=0)

box1 = Entry(window)
box1.grid(row=0,column=2)


Butto = Button(window,text="ADD",command=lambda:op('+'))
#Butto.pack()
Butto.grid(row=1,column=0)

Butto1 = Button(window,text="SUBTRACT",command=lambda:op('-'))
#Butto.pack()
Butto1.grid(row=1,column=1)

Butto2 = Button(window,text="MUL",command=lambda:op('*'))
#Butto.pack()
Butto2.grid(row=1,column=2)

Butto3 = Button(window,text="DIVI",command=lambda:op('/'))
#Butto.pack()
Butto3.grid(row=1,column=3)

Button1 = Button(window,text="CLOSE",command=window.destroy)
#Button1.pack()
Button1.grid(row=3,column=0)
l1 = Label(window,textvariable=s)
l1.grid(row=4,column=0)

Butto = Button(window,text="EVALUATE",bd=3,command= spch )
Butto.grid(row=6,column=0)

window.mainloop() 