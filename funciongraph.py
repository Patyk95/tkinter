import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
from math import *
window=tk.Tk()


# def func(func,min,max,step):
#     data=np.arange(min,max,step)
#     func




data=np.arange(-10,30,2)
print(data)

cyfry=np.arange(-10,10,2)

def plotowanie(x):
    f=(x**2+ sqrt(x))
    return np.vectorize(f)


plt.plot(cyfry,plotowanie(cyfry))
plt.show()





window.geometry('850x300')
window.title("Ploting your graph absed on given function")
window.config(background='green')

func_label=tk.Label(window,text='Please pass your funcion: ',font=('arial',20),width=24)
func_label.grid(row=0,column=0,padx=10,pady=10)
func_button=tk.Entry(window,font=('arial',20))
func_button.grid(row=0,column=1,padx=10,pady=10)
min_label=tk.Label(window,text='Please choose your min value: ',font=('arial',20),width=24)
min_label.grid(row=1,column=0,padx=10,pady=10)
min_button=tk.Spinbox(window,from_=-100,to=100,font=('arial',18))
min_button.grid(row=1,column=1,padx=10,pady=10)
max_label=tk.Label(window,text='Please choose your max value: ',font=('arial',20),width=24)
max_label.grid(row=2,column=0,padx=10,pady=10)
max_button=tk.Spinbox(window,from_=-100,to=100,font=('arial',18))
max_button.grid(row=2,column=1,padx=10,pady=10)
step_label=tk.Label(window,text='Please choose step for values: ',font=('arial',20),width=24)
step_label.grid(row=3,column=0,padx=10,pady=10)
step_button=tk.Spinbox(window,from_=-10.0,to=10.0,font=('arial',18))
step_button.grid(row=3,column=1,padx=10,pady=10)

draw=tk.Button(window,text="Draw",font=('arial',20),background='red',width=10)
draw.grid(row=4,column=1)






window.mainloop()
