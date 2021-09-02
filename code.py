import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import tkinter.font as tkFont
from functools import partial  

window = tk.Tk()
window.geometry("340x500")
window.title("Calculater")
window.configure(bg="#515a5a")

frame0=tk.Frame(master=window,width=340,height=500,bg="#282828")


entry=tk.Entry(master = frame0,width=12,fg="white",bg="#282828",border=0,font=tkFont.Font(family="Helvetica",size=35,weight="bold"))
entry.place(x=10,y=50)

operations=[]
numbers=[]
    
def Ac():
    entry.delete(0, tk.END)
    operations.clear()
    numbers.clear()
def sr():
    summ = entry.get()
    entry.delete(0,tk.END)
    entry.insert(tk.END,float(summ)*float(summ))
def roo():
    num=entry.get()
    entry.delete(0,tk.END)
    numbers.append(float(num))
    operations.append("^")
def bks():
    num=entry.get()
    entry.delete(len(num)-1,tk.END)
def one():
    entry.insert(tk.END,"1")
def two():
    entry.insert(tk.END,"2")
def thr():
    entry.insert(tk.END,"3")
def fou():
    entry.insert(tk.END,"4")
def fiv():
    entry.insert(tk.END,"5")
def six():
    entry.insert(tk.END,"6")
def sev():
    entry.insert(tk.END,"7")
def eig():
    entry.insert(tk.END,"8")
def nin():
    entry.insert(tk.END,"9")
def ser():
    entry.insert(tk.END,"0")
def poi():
    entry.insert(tk.END,".")
def plus():
    num = (entry.get())
    numbers.append(float(num))
    operations.append("+")
    entry.delete(0,tk.END)
    if len(num)>1:
        solve()
def minerse():
    num = entry.get()
    numbers.append(float(num))
    operations.append("-")
    entry.delete(0,tk.END)
    if len(num)>1:
        solve()
def multiply():
    num = entry.get()
    numbers.append(float(num))
    operations.append("*")
    entry.delete(0,tk.END)
    if len(num)>1:
        solve()
def division():
    num = entry.get()
    numbers.append(float(num))
    operations.append("/")
    entry.delete(0,tk.END)
    if len(num)>1:
        solve()
def equal():
    num = entry.get()
    numbers.append(float(num))
    entry.delete(0,tk.END)
    if len(numbers) >= 2:
        solve()
    numbers.clear()
    operations.clear()
    
def solve():
    j=numbers[0]
    result=0
    for i in range(len(numbers)-1):
        if operations[i]=="+":
            float(result)
            result = numbers[i]+numbers[i+1] 
        elif operations[i]=="-":
            float(result)
            result = numbers[i]-numbers[i+1] 
        elif operations[i]=="*":
            float(result)
            result = numbers[i]*numbers[i+1] 
        elif operations[i]=="/":
            float(result)
            result = numbers[i]/numbers[i+1] 
        elif operations[i]=="^":
            float(result)
            result = numbers[i]**numbers[i+1]
    if result!=0:
        entry.delete(0,tk.END)
        entry.insert(tk.END,str(result))

buttonGrid = ["AC","X^2","^","Backspace","1","2","3","+","4","5","6","-","7","8","9","*",".","0","=","/"]
colorList = ["#56a8ff","#414141","#414141","#b30000","Black","Black","Black","#414141","Black","Black","Black","#414141","Black","Black","Black","#414141","#414141","Black","#ff2020","#414141"]
commandlist = [Ac,sr,roo,bks,one,two,thr,plus,fou,fiv,six,minerse,sev,eig,nin,multiply,poi,ser,equal,division]
    
counter=0
w,h=9,3
f,e=7*w,28*h
g = e-80
gg = f+100
for i in range(1,6):
    for ii in range(1,5):
        button=tk.Button(master=frame0,
                         text=buttonGrid[counter],
                         bg=colorList[counter],
                         fg="white",
                         font=tkFont.Font(family="Helvetica",size=10,weight="bold"),
                         width=w,
                         height=h,
                         border=0,
                         command=commandlist[counter]
                         )
        button.place(x=g,y=gg)
        counter+=1
        g += e
        
    g=e-80
    gg+=f
frame0.place(x=0,y=0)



window.mainloop()
