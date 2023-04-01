import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
from math import *
import pandas as pd
from tkinter.messagebox import showerror
window=tk.Tk()



def plot():
    
    min=min_button.get()
    max=max_button.get()
    funkcja=func_button.get()
    wklad=np.linspace(int(min),int(max))
    wynik=[]
    try:
        for x in wklad:
            wynik.append((eval(funkcja)))
    except SyntaxError:
        showerror("Fault",'Please check your function!!!')
    except NameError:
        showerror("Fault",'Please provide only X !!!')
    plt.plot(wynik)
    plt.title(f'Graph for your funcion : {funkcja}')

    plt.show()    

def export():
    min=min_button.get()
    max=max_button.get()
    funkcja=func_button.get()
    wklad=np.linspace(int(min),int(max))
    wynik=[]
    for x in wklad:
        wynik.append((eval(funkcja)))
    frame=pd.DataFrame(wynik)
    frame.to_excel('Results_for_my_funcion.xlsx')
    print(frame)
    
    


    

window.geometry('850x350')
window.title("Ploting your graph based on given function")
window.config(background='green')

func_label=tk.Label(window,text='Please pass your funcion: ',font=('arial',20),width=24)
func_label.grid(row=0,column=0,padx=10,pady=10)
func_button=tk.Entry(window,font=('arial',20))
func_button.grid(row=0,column=1,padx=10,pady=10)
min_label=tk.Label(window,text='Please choose your min value: ',font=('arial',20),width=24)
min_label.grid(row=1,column=0,padx=10,pady=10)
min_button=tk.Spinbox(window,from_=-100,to=10,font=('arial',18))
min_button.grid(row=1,column=1,padx=10,pady=10)
max_label=tk.Label(window,text='Please choose your max value: ',font=('arial',20),width=24)
max_label.grid(row=2,column=0,padx=10,pady=10)
max_button=tk.Spinbox(window,from_=-100,to=100,font=('arial',18))
max_button.grid(row=2,column=1,padx=10,pady=10)

draw=tk.Button(window,text="Draw",command=plot,font=('arial',20),background='red',width=10)
draw.grid(row=3,column=1)

draw=tk.Button(window,text="Export Results",command=export,font=('arial',20),background='orange',width=14)
draw.grid(row=4,column=1,pady=20)






window.mainloop()
