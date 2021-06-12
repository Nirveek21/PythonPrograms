from  tkinter import *
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
window = Tk() # instantiate a window instance
window.title("GUI TEST")
window.geometry('1600x800')

s = StringVar()
age = StringVar()
icon= PhotoImage(file='logo.png')
window.iconphoto(TRUE,icon)

def op():
    df = pd.read_csv('heart.csv')
    X=df[['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']]
    y=df['target']

    x_test,x_train,y_test,y_train = train_test_split(X,y,test_size = 0.25,random_state = 1)

    lr = LogisticRegression()
    lr.fit(x_train,y_train)
    #y_prediction=lr.predict(x_test)
    chance=lr.predict([[int(a.get()),int(sx.get()),int(Cp.get()),int(Rbp.get()),int(Sc.get()),int(Fbs.get()),int(Recg.get()),int(Mhr.get()),int(Eia.get()),float(Op.get()),int(St.get()),int(Nmf.get()),int(thal.get())]])
    #print(x_test)
    #print(y_prediction)
    #print("Accuracy : ",lr.score(x_test,y_test))
    if(chance==1):
        s.set('You have chances of Heart attack')
    else:
        s.set('Nothing to worry about')
Label(window, text='Enter your details').grid(row=0)
Label(window, text='Age :').grid(row=1)
a = Entry(window )
a.grid(row=1,column=1)

Label(window, text='Sex :').grid(row=2)
sx = Entry(window )
sx.grid(row=2,column=1)

Label(window, text='Chest pain').grid(row=3)
Cp = Entry(window )
Cp.grid(row=3,column=1)

Label(window, text='Resting Blood Pressure').grid(row=4)
Rbp = Entry(window )
Rbp.grid(row=4,column=1)

Label(window, text='Cholestrol').grid(row=5)
Sc = Entry(window )
Sc.grid(row=5,column=1)

Label(window, text='Fasting Blood Sugar').grid(row=6)
Fbs = Entry(window )
Fbs.grid(row=6,column=1)

Label(window, text='Resting Elec-Cardiograph').grid(row=7)
Recg = Entry(window )
Recg.grid(row=7,column=1)

Label(window, text='Maximum Heart Rate').grid(row=8)
Mhr = Entry(window )
Mhr.grid(row=8,column=1)

Label(window, text='Exercise induced angina').grid(row=9)
Eia = Entry(window )
Eia.grid(row=9,column=1)

Label(window, text='Oldpeak').grid(row=10)
Op = Entry(window )
Op.grid(row=10,column=1)

Label(window, text='Slope of peak exercise(ST)').grid(row=11)
St = Entry(window )
St.grid(row=11,column=1)

Label(window, text='Number of major vessels').grid(row=12)
Nmf = Entry(window )
Nmf.grid(row=12,column=1)

Label(window, text='Thalassemia').grid(row=13)
thal = Entry(window )
thal.grid(row=13,column=1)

Butto = Button(window,text="OPEN",command=lambda:op())
#Butto.pack()
Butto.grid(row=14,column=0)
Button1 = Button(window,text="CLOSE",command=window.destroy)
#Button1.pack()
Button1.grid(row=15,column=0)
l1 = Label(window,textvariable=s)
l1.grid(row=16,column=0)

window.mainloop()
