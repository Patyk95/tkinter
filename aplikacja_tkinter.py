from tkinter import *
import tkinter as tk
import sqlite3

con = sqlite3.connect("my_database")
cur = con.cursor()
cur.execute("create table lista_studentów('Imię','Nazwisko','Kierunek Studiów','Index')")

def zapisz():
    #auto cleaning etry fields

    #creating connection with db
    con = sqlite3.connect("my_database")
    cur = con.cursor()
    #inserting data into db
    cur.execute("insert into lista_studentów values (:ei,:en,:ek,:ei1)",
                {
                    'ei': ei.get(),
                    'en': en.get(),
                    'ek': ek.get(),
                    'ei1': ei1.get()
                 })
    con.commit()
    ei.delete(0, END)
    en.delete(0, END)
    ek.delete(0, END)
    ei1.delete(0, END)

def show():
    con = sqlite3.connect("my_database")
    cur = con.cursor()
    cur.execute('select *,oid from lista_studentów')
    z = cur.fetchall()
    print(z)

    con.commit()
    con.close()

def delete():
    con = sqlite3.connect("my_database")
    cur = con.cursor()
    cur.execute('drop table lista_studentów')
    con.commit()
    con.close()


window = tk.Tk()
window.geometry('550x120')
i = tk.Label (window, text='Imię').grid(row=0)
ei = tk.Entry(window)
ei.grid(row=0, column=1)
n = tk.Label (window, text='Nazwisko').grid(row=1)
en = tk.Entry(window)
en.grid(row=1, column=1)
k = tk.Label (window, text='Kierunek studiów').grid(row=2)
ek = tk.Entry(window)
ek.grid(row=2, column=1)
i1 = tk.Label (window, text='Numer indexu').grid(row=3)
ei1 = tk.Entry(window)
ei1.grid(row=3, column=1)


tk.Button(window, text="Wyjdź", command=window.quit).grid(row=4, column=0, sticky=tk.W, pady=4)
tk.Button(window, text="Dodaj Pozycję", command=zapisz).grid(row=4, column=1, sticky=tk.W, pady=4)
tk.Button(window, text="Wyświetl Pozycję", command=show).grid(row=4, column=2, sticky=tk.W, pady=4)
tk.Button(window, text="Wyczyść Tabelę", command=delete).grid(row=4, column=3, sticky=tk.W, pady=4)
window.mainloop()

