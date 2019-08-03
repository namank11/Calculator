from tkinter import *
import math
cal=Tk()
cal.title("Calculator")
operator=""
inputv=StringVar()
def btnroot():
    global operator
    operator = str(math.sqrt(int(operator)))
    inputv.set(operator)
def btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    inputv.set(operator)
def btnclear():
    global operator
    operator=operator[:-1]
    inputv.set(operator)
def btnaclear():
    global operator
    operator = ""
    inputv.set("")
def equate():
    global operator
    sumup=str(eval(operator))
    inputv.set(sumup)
Field=Entry(cal,font=('arial',20,'bold'),textvariable=inputv,bd=15,insertwidth=5,bg='orange',justify='right').grid(columnspan=5)
btn7=Button(cal,padx=16,pady=16,bd=4,fg='black',font=('arial',10,'bold'),text='7',bg='orange',command=lambda:btnclick(7)).grid(row=1,column=0);
btn8=Button(cal,padx=16,pady=16,bd=4,fg='black',font=('arial',10,'bold'),text='8',bg='orange',command=lambda:btnclick(8)).grid(row=1,column=1);
btn9=Button(cal,padx=16,pady=16,bd=4,fg='black',font=('arial',10,'bold'),text='9',bg='orange',command=lambda:btnclick(9)).grid(row=1,column=2);
btncl=Button(cal,padx=16,pady=16,bd=4,fg='black',font=('arial',10,'bold'),text='CL',bg='orange',command=lambda:btnclear()).grid(row=1,column=3);
btnuroot=Button(cal,padx=16,pady=16,bd=4,fg='black',font=('arial',10,'bold'),text='Sqrt',bg='orange',command=lambda:btnroot()).grid(row=1,column=4);
######################################################################################################################################
btn4=Button(cal,padx=16,pady=16,bd=4,fg='black',font=('arial',10,'bold'),text='4',bg='orange',command=lambda:btnclick(4)).grid(row=2,column=0);
btn5=Button(cal,padx=16,pady=16,bd=4,fg='black',font=('arial',10,'bold'),text='5',bg='orange',command=lambda:btnclick(5)).grid(row=2,column=1);
btn6=Button(cal,padx=16,pady=16,bd=4,fg='black',font=('arial',10,'bold'),text='6',bg='orange',command=lambda:btnclick(6)).grid(row=2,column=2);
btnclr=Button(cal,padx=16,pady=16,bd=4,fg='black',font=('arial',10,'bold'),text='AC',bg='orange',command=lambda:btnaclear()).grid(row=2,column=3);
btnpow=Button(cal,padx=16,pady=16,bd=4,fg='black',font=('arial',10,'bold'),text='Pow',bg='orange',command=lambda:btnclick("**")).grid(row=2,column=4);
######################################################################################################################################
btn1=Button(cal,padx=16,pady=16,bd=4,fg='black',font=('arial',10,'bold'),text='1',bg='orange',command=lambda:btnclick(1)).grid(row=3,column=0);
btn2=Button(cal,padx=16,pady=16,bd=4,fg='black',font=('arial',10,'bold'),text='2',bg='orange',command=lambda:btnclick(2)).grid(row=3,column=1);
btn3=Button(cal,padx=16,pady=16,bd=4,fg='black',font=('arial',10,'bold'),text='3',bg='orange',command=lambda:btnclick(3)).grid(row=3,column=2);
btnadd=Button(cal,padx=16,pady=16,bd=4,fg='black',font=('arial',10,'bold'),text='+',bg='orange',command=lambda:btnclick("+")).grid(row=3,column=3);
btnadd=Button(cal,padx=16,pady=16,bd=4,fg='black',font=('arial',10,'bold'),text='.',bg='orange',command=lambda:btnclick(".")).grid(row=3,column=4);
######################################################################################################################################
btnsub=Button(cal,padx=16,pady=16,bd=4,fg='black',font=('arial',10,'bold'),text='-',bg='orange',command=lambda:btnclick("-")).grid(row=4,column=0);
btneq=Button(cal,padx=16,pady=16,bd=4,fg='black',font=('arial',10,'bold'),text='=',bg='orange',command=lambda:equate()).grid(row=4,column=1);
btnmul=Button(cal,padx=16,pady=16,bd=4,fg='black',font=('arial',10,'bold'),text='X',bg='orange',command=lambda:btnclick("*")).grid(row=4,column=2);
btndiv=Button(cal,padx=16,pady=16,bd=4,fg='black',font=('arial',10,'bold'),text='/',bg='orange',command=lambda:btnclick("/")).grid(row=4,column=3);
btnadd=Button(cal,padx=16,pady=16,bd=4,fg='black',font=('arial',10,'bold'),text='0',bg='orange',command=lambda:btnclick("0")).grid(row=4,column=4);
cal.mainloop()
