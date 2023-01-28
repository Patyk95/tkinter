from tkinter import *
import sqlite3
from datetime import datetime

import xlsxwriter

from time import strftime
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from xlsxwriter.workbook import Workbook




#connection and database
con=sqlite3.connect('prodcution_db')
cur=con
cur.execute("create table  if not exists status_produkcji('id' integer primary key autoincrement,product not null, qty,date,employee,additional_info,shift)")
#cur.execute("drop table status_produkcji")


#Gui
window=Tk()
window.title('PRODUCTION MANAGEMENT SYSTEM')
window.geometry("850x600")
window.configure(background="#ede9c4")
#Part number

def time():
    d = datetime.today()
    d2 = d.strftime('%Y-%m-%d')
    t2 = strftime("%H:%M:%S")
    lbl1.config(text="Current Day And Time Is:  " + d2 +" " + t2)
    lbl1.after(1000,time)

dkx = datetime.today()
dkx1=dkx.strftime('%Y-%m-%d,%H :%M :%S')
dkx2=dkx.strftime('%Y-%m-%d')
def confirmation():
    con = sqlite3.connect('prodcution_db')
    cur = con
    cur.execute("insert into status_produkcji(product,shift,qty,date,employee,additional_info) values(:product,:shift,:qty,:date,:employee,:additional_info)",
                {
                    'product':b1.get(),
                    'shift':b8.get(),
                    'qty':b2.get(),
                    'date':dkx2,
                    'employee':b3.get(),
                    'additional_info':b4.get()
                                        })
    con.commit()
    b1.delete(0,END)
    b2.delete(0, END)
    b3.delete(0, END)
    b4.delete(0, END)
    b8.delete(0, END)

def reject():
    b1.delete(0, END)
    b2.delete(0, END)
    b3.delete(0, END)
    b4.delete(0, END)
    b8.delete(0, END)

def check_if_empty():
    if b1.get() and b2.get() and b3.get() and b8.get()<'4' :
        confirmation()
    else:
        tk.messagebox.showerror("ERROR","At Least Number of Product, Personal ID, Nuber, Shift and  Qty Have To Be Provided")


def show_my():
    if b3.get():
        show_my_results()
    else:
        tk.messagebox.showerror('Error','Personal Number Must Be Filled')


def show_my_results():
    window = tk.Tk()
    window.title('My Results')
    window.geometry('1250x800')
    # define columns
    columns = ('c1','c2','c3','c4','c5','c6','c7')
    tree = ttk.Treeview(window, columns=columns, show='headings', height=52)
    # define headings
    tree.heading('c1', text='ID')
    tree.heading('c2', text='Date')
    tree.heading('c3', text='Shift')
    tree.heading('c4', text='Part Number')
    tree.heading('c5', text='Qty')
    tree.heading('c6', text='Personal ID')
    tree.heading('c7', text='Comments')


    # add data to the treeview
    con = sqlite3.connect('prodcution_db')
    cur = con
    for row in cur.execute('select id,date,shift,product,qty,employee,additional_info from status_produkcji where employee = :employee' ,{
           'employee':b3.get()
           }):
        tree.insert('', tk.END, values=(row[0], row[1], row[2],row[3],row[4],row[5],row[6]))
        tree.grid(row=0, column=0, sticky='nsew')
        # add a scrollbar
        scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
        con.commit()


def export_to_excel():
    workbook = Workbook('archiwum.xlsx')
    worksheet = workbook.add_worksheet()
    con = sqlite3.connect('prodcution_db')
    c = con.cursor()
    con.execute("select * from status_produkcji")
    mysel = c.execute("select * from status_produkcji")
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            worksheet.write(i, j, row[j])
    workbook.close()
    window.destroy()


text=Text(window,height=20,width=40)
l1=Label(window,text='Please Fill Produced Part Number',font=("arial",15),background='white')
l1.grid(padx=20,pady=20,row=1,column=1)
b1=Entry(window,width=25,font=('arial',15))
b1.grid(padx=20,pady=20,column=2,row=1)
#Produced qty
l2=Label(window,text='Please Fill Qty Of Produced Part Number',font=("arial",15),background='white')
l2.grid(padx=20,pady=20,row=2,column=1)
b2=Entry(window,width=25,font=('arial',15))
b2.grid(padx=20,pady=20,column=2,row=2)
#Worker details
l3=Label(window,text='Please Fill Your Employee Number',font=("arial",15),background='white')
l3.grid(padx=20,pady=20,row=3,column=1)
b3=Entry(window,width=25,font=('arial',15))
b3.grid(padx=20,pady=20,row=3,column=2)
lbl1 = Label(window, font=('Arial', 15), background='white', foreground='black')   # wyswietalnie czasu
lbl1.grid(row=0, column=1, padx=40, pady=20)
time()

l4=Label(window,text='Please Add Any Info [Optional]',font=("arial",15),background='white')
l4.grid(padx=20,pady=20,row=4,column=1)
b4=Entry(window,width=25,font=('arial',15))
b4.grid(padx=20,pady=20,row=4,column=2)
b5=Button(window,text="Confirm And Add",command=check_if_empty,font=("arial",20),background="green")
b5.grid(row=7,column=1)
b6=Button(window,text="Reject",command=reject,font=("arial",20),background="red")
b6.grid(row=7,column=2,pady=25)
b7=Button(window,text="Show Your Results",command=show_my,font=("arial",20),background="Orange")
b7.grid(row=8,column=2)
b9=Button(window,text="Export To Excel",command=export_to_excel,font=("arial",20),background="Blue")
b9.grid(row=8,column=1)
b8=Entry(window,font=('arial',15),width=25)
b8.grid(row=6,column=2,pady=15)
l8=Label(window,text="Please Entry Shift Number",font=('arial',15),bg='white')
l8.grid(row=6,column=1)

window.mainloop()

