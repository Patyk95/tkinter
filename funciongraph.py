import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
from math import *
import pandas as pd
from tkinter.messagebox import showerror

window=tk.Tk()

window.geometry('350x250')
window.title("Ploting your graph based on given function")
Label=tk.Label(window,text="Please choose variant from menu",font=('Arial',15))
Label.grid(row=0,column=0,padx=20,pady=20)
window.config(background='green')


    
def funkx():
    window.geometry('800x350')

    def export():
        min=min_x_button.get()
        max=max_x_button.get()
        funkcja=func_button.get()
        wklad=np.linspace(float(min),float(max))
        wynik=[]
        for x in wklad:
            wynik.append((eval(funkcja)))
        frame=pd.DataFrame(wynik)
        frame.to_excel('Results_for_my_funcion.xlsx')
        print(frame)

    def plot():
        min_x=min_x_button.get()
        max_x=max_x_button.get()
        funkcja=func_button.get()
        wklad_x=np.linspace(float(min_x),float(max_x))
        wynik=[]
        try:
            for x in wklad_x:
                wynik.append((eval(funkcja)))
        except SyntaxError:
            showerror("Fault",'Please check your function!!!')
        except NameError:
            showerror("Fault",'Please provide only X !!!')
        plt.plot(wynik)
        plt.title(f'Graph for your funcion : {funkcja}')

        plt.show()    

    func_label=tk.Label(window,text='Please pass your funcion: ',font=('arial',20),width=20)
    func_label.grid(row=0,column=0,padx=10,pady=10,sticky='w')
    func_button=tk.Entry(window,font=('arial',20))
    func_button.grid(row=0,column=1,padx=10,pady=10,sticky='e')
    x_label=tk.Label(window,text='Please choose your X range: ',font=('arial',20))
    x_label.grid(row=1,column=0,padx=10,pady=10,sticky='w')
    min_x_button=tk.Entry(window,font=('arial',20),width=5)
    min_x_button.grid(row=1,column=1,padx=10,pady=10,sticky='w')
    max_x_button=tk.Entry(window,font=('arial',20),width=5)
    max_x_button.grid(row=1,column=1,padx=10,pady=10,sticky='e')

    draw=tk.Button(window,text="Draw",command=plot,font=('arial',20),background='red',width=10)
    draw.grid(row=4,column=0)

    draw=tk.Button(window,text="Export Results",command=export,font=('arial',20),background='orange',width=14)
    draw.grid(row=4,column=1,pady=20)

def funncxy():
    window.geometry('800x350')

    def export():
        min_x=min_x_button.get()
        max_x=max_x_button.get()
        min_y=min_y_button.get()
        max_y=max_y_button.get()
        funkcja=func_button.get()
        wklad_x=np.linspace(float(min_x),float(max_x))
        wklad_y= np.linspace(float(min_y),float(max_y))
        wynik=[]
        for x in wklad_x:
            for y in wklad_y:
                wynik.append((eval(funkcja)))
        frame=pd.DataFrame(wynik)
        frame.to_excel('Results_for_my_funcion.xlsx')
        print(frame)

    def plot():
        min_x=min_x_button.get()
        max_x=max_x_button.get()
        min_y=min_y_button.get()
        max_y=max_y_button.get()
        funkcja=func_button.get()
        wklad_x=np.linspace(float(min_x),float(max_x))
        wklad_y= np.linspace(float(min_y),float(max_y))
        wynik=[]
        try:
            for x in wklad_x:
                for y in wklad_y:
                    wynik.append((eval(funkcja)))
        except SyntaxError:
            showerror("Fault",'Please check your function!!!')
        except NameError:
            showerror("Fault",'Please provide only X and Y !!!')
        plt.plot(wynik)
        plt.title(f'Graph for your funcion : {funkcja}')

        plt.show()    

    func_label=tk.Label(window,text='Please pass your funcion: ',font=('arial',20),width=20)
    func_label.grid(row=0,column=0,padx=10,pady=10,sticky='w')
    func_button=tk.Entry(window,font=('arial',20))
    func_button.grid(row=0,column=1,padx=10,pady=10,sticky='e')
    x_label=tk.Label(window,text='Please choose your X range: ',font=('arial',20))
    x_label.grid(row=1,column=0,padx=10,pady=10,sticky='w')
    min_x_button=tk.Entry(window,font=('arial',20),width=5)
    min_x_button.grid(row=1,column=1,padx=10,pady=10,sticky='w')
    max_x_button=tk.Entry(window,font=('arial',20),width=5)
    max_x_button.grid(row=1,column=1,padx=10,pady=10,sticky='e')
    y_label=tk.Label(window,text='Please choose your Y range: ',font=('arial',20))
    y_label.grid(row=2,column=0,padx=10,pady=10)
    min_y_button=tk.Entry(window,font=('arial',20),width=5)
    min_y_button.grid(row=2,column=1,padx=10,pady=10,sticky='w')
    max_y_button=tk.Entry(window,font=('arial',20),width=5)
    max_y_button.grid(row=2,column=1,padx=10,pady=10,sticky='e')
    

    draw=tk.Button(window,text="Draw",command=plot,font=('arial',20),background='red',width=10)
    draw.grid(row=4,column=0)

    draw=tk.Button(window,text="Export Results",command=export,font=('arial',20),background='orange',width=14)
    draw.grid(row=4,column=1,pady=20)

def funncxyz():
    window.geometry('800x350')

    def export():
        min_x=min_x_button.get()
        max_x=max_x_button.get()
        min_y=min_y_button.get()
        max_y=max_y_button.get()
        min_z=min_z_button.get()
        max_z=max_z_button.get()
        funkcja=func_button.get()
        wklad_x=np.linspace(float(min_x),float(max_x))
        wklad_y= np.linspace(float(min_y),float(max_y))
        wklad_z= np.linspace(float(min_z),float(max_z))

        wynik=[]
        for x in wklad_x:
            for y in wklad_y:
                for z in wklad_z:
                    wynik.append((eval(funkcja)))
        frame=pd.DataFrame(wynik)
        frame.to_excel('Results_for_my_funcion.xlsx')
        print(frame)

    def plot():
        min_x=min_x_button.get()
        max_x=max_x_button.get()
        min_y=min_y_button.get()
        max_y=max_y_button.get()
        min_z=min_z_button.get()
        max_z=max_z_button.get()
        funkcja=func_button.get()
        wklad_x=np.linspace(float(min_x),float(max_x))
        wklad_y= np.linspace(float(min_y),float(max_y))
        wklad_z= np.linspace(float(min_z),float(max_z))
        wynik=[]
        try:
            for x in wklad_x:
                for y in wklad_y:
                    for z in wklad_z:
                        wynik.append((eval(funkcja)))
        except SyntaxError:
            showerror("Fault",'Please check your function!!!')
        except NameError:
            showerror("Fault",'Please provide only X !!!')
        plt.plot(wynik)
        plt.title(f'Graph for your funcion : {funkcja}')

        plt.show()    

    func_label=tk.Label(window,text='Please pass your funcion: ',font=('arial',20),width=20)
    func_label.grid(row=0,column=0,padx=10,pady=10,sticky='w')
    func_button=tk.Entry(window,font=('arial',20))
    func_button.grid(row=0,column=1,padx=10,pady=10,sticky='e')
    x_label=tk.Label(window,text='Please choose your X range: ',font=('arial',20))
    x_label.grid(row=1,column=0,padx=10,pady=10,sticky='w')
    min_x_button=tk.Entry(window,font=('arial',20),width=5)
    min_x_button.grid(row=1,column=1,padx=10,pady=10,sticky='w')
    max_x_button=tk.Entry(window,font=('arial',20),width=5)
    max_x_button.grid(row=1,column=1,padx=10,pady=10,sticky='e')
    y_label=tk.Label(window,text='Please choose your Y range: ',font=('arial',20))
    y_label.grid(row=2,column=0,padx=10,pady=10)
    min_y_button=tk.Entry(window,font=('arial',20),width=5)
    min_y_button.grid(row=2,column=1,padx=10,pady=10,sticky='w')
    max_y_button=tk.Entry(window,font=('arial',20),width=5)
    max_y_button.grid(row=2,column=1,padx=10,pady=10,sticky='e')
    z_label=tk.Label(window,text='Please choose your Z range: ',font=('arial',20))
    z_label.grid(row=3,column=0,padx=10,pady=10)
    min_z_button=tk.Entry(window,font=('arial',20),width=5)
    min_z_button.grid(row=3,column=1,padx=10,pady=10,sticky='w')
    max_z_button=tk.Entry(window,font=('arial',20),width=5)
    max_z_button.grid(row=3,column=1,padx=10,pady=10,sticky='e')
    

    draw=tk.Button(window,text="Draw",command=plot,font=('arial',20),background='red',width=10)
    draw.grid(row=4,column=0)

    draw=tk.Button(window,text="Export Results",command=export,font=('arial',20),background='orange',width=14)
    draw.grid(row=4,column=1,pady=20)

menubar= Menu()
    
filemenu = Menu(menubar, tearoff=0, background='#ffcc99', foreground='black')
filemenu.add_command(label='Funcion only with X',command=funkx)
filemenu.add_command(label='Funcion with X and Y',command=funncxy)
filemenu.add_command(label='Funcion with X, Y and Z',command=funncxyz)
filemenu.add_separator()
filemenu.add_command(label='Close window',command=window.quit)
menubar.add_cascade(label="Function Options",menu=filemenu)
window.config(menu=menubar)



window.mainloop()


