import sys
from tkinter import *
from time import strftime
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time
import datetime
import sqlite3
import calendar
from datetime import datetime
from tkinter import ttk
import tkinter as tk


# creating employee dbbms
con = sqlite3.connect(" overtime_db ")
cur = con.cursor()

cur.execute("create table if not exists wejscie('id' integer primary key autoincrement,'numer_pers' not null,'dzień','godzina_rozpoczęcia')")
cur.execute("create table if not exists wyjscie('id' integer primary key autoincrement,'numer_pers' not null,'dzień','godzina_zakończenia')")
#cur.execute("drop table wyjscie")
#cur.execute("drop table wejscie")

# creating an object of tkinter
window = Tk()


window.title("Czas pracy")
window.geometry("650x450")
#Background

# img=Image.open("C:\\Users\\prajt\\Desktop\\tlo.jpg")
# tlo = ImageTk.PhotoImage(img)
# tlo_lbl=Label(window,image=tlo)
# tlo_lbl.place(x=0,y=0)


czas=time.gmtime()
w=calendar.timegm(czas)
date_time = datetime.fromtimestamp(w)
czas_to_date = date_time.strftime("%d-%m-%Y %H:%M:%S")


def czas():
    godzina = strftime('%H : %M : %S')
    lbl_godz.config(text="Aktualna godzina to: " + godzina)
    lbl_godz.after(1000, czas)


def data():
    dzien = strftime('%d - %m - %Y')
    lbl_dzien.config(text="Jest: " + dzien)

def check_numer():
    if num_pers.get():
        start()
    else:
        tk.messagebox.showerror('Numer Personalny Musi Być Podany',"Brak Numeru Praconika-Zacznij Ponownie")


def check_numer1():
    if num_pers.get():
        koniec()
    else:
        tk.messagebox.showerror('Numer Personalny Musi Być Podany',"Brak Numeru Praconika-Zacznij Ponownie")


def start():
    czas = time.gmtime()
    w = calendar.timegm(czas)
    date_time = datetime.fromtimestamp(w)
    data = date_time.strftime("%d-%m-%Y ")
    date_format_str = '%d-%m-%Y %H:%M:%S'
    start = datetime.strptime(czas_to_date, date_format_str)
    con = sqlite3.connect(" overtime_db ")
    cur = con.cursor()
    cur.execute("insert into wejscie ('numer_pers','dzień','godzina_rozpoczęcia')values(:num,:dz,:godz)",
        {
        'num': num_pers.get(),
        'dz': data,
        'godz': start
        })
    num_pers.delete(0, END)
    messagebox.showinfo(title="Rozpoczęcie pracy", message='Dodano czas rozpoczęcia pracy')
    con.commit()


def koniec():
    czas = time.gmtime()
    w = calendar.timegm(czas)
    date_time = datetime.fromtimestamp(w)
    data = date_time.strftime("%d-%m-%Y ")
    date_format_str = '%d-%m-%Y %H:%M:%S'
    end = datetime.strptime(czas_to_date, date_format_str)
    con = sqlite3.connect(" overtime_db ")
    cur = con.cursor()
    try:
        cur.execute("insert into wyjscie ('numer_pers','dzień','godzina_zakończenia') values(:num,:dz,:godz)",
            {
                'num': num_pers.get(),
                'dz': data,
                'godz': end
            })
    except sqlite3.OperationalError:
        tk.messagebox.showerror('Numer Personalny Musi Być Podany',"Brak Numeru Praconika-Zacznij Ponownie")
        sys.exit()
    con.commit()
    num_pers.delete(0,END)
    messagebox.showinfo(title="Zakończenie pracy", message='Dodano czas ukończenia pracy')


#labels and buttons


lbl_godz = Label(window, font=('Arial', 30), background='white', foreground='black')   # wyswietalnie czasu
lbl_godz.grid(row=2, column=0, padx=20, pady=20)
czas()

lbl_dzien = Label(window, font=('arial', 30),background='white',foreground='black')  # data-wyświetlanie daty na gui
lbl_dzien.grid(row=3, column=0)
data()

mystr=StringVar()
mystr.set('Uzupełnij numer personalny w innym wypadku czas nie będzie naliczonoy')


num_pers = Entry(window, font=('arial', 30))
num_pers.grid(row=1, column=0, pady=10, padx=10)  # num_personalny

num_personalny_label = Label(window, text='Wprowadź swój numer identyfikacyjny: ',font=("arial", 20),background='white',foreground='black').grid(row=0,column=0,pady=10)

num_personalny_label1=Label(window,text='Numer pracowniczy musi być podany by odnotować czas',font=("arial",15),background='red',foreground='yellow').grid(row=7,column=0)

b1=Button(window,text="Rozpocznij pracę",command=check_numer,width=20).grid(row=5,column=0,padx=20,pady=30,sticky='W')


b2=Button(window,text="Zakończ pracę",command=check_numer1,width=20).grid(row=5,column=0,padx=20,pady=30,sticky='E')




#***********************************************

def explore_entry():
    window = tk.Tk()
    window.title('Baza Wejść')
    window.geometry('830x1000')
    # define columns
    columns = ('c1','c2','c3', 'c4')
    tree = ttk.Treeview(window, columns=columns, show='headings',height=52)
    # define headings
    tree.heading('c1', text='Numer Wiersza')
    tree.heading('c2', text='Numer Pracownika')
    tree.heading('c3', text='Data Rozpoczęcia Pracy')
    tree.heading('c4', text='Godzina Rozpoczęcia Pracy')
    # add data to the treeview
    cur.execute("select * from wejscie")
    rows = cur.fetchall()
    for row in rows:
        tree.insert('', tk.END, values=(row[0],row[1],row[2],row[3]))
    tree.grid(row=0, column=0, sticky='nsew')
    # add a scrollbar
    scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')


def expolre_exit():
    window = tk.Tk()
    window.title('Baza Wyjść')
    window.geometry('830x1000')
    # define columns
    columns = ('c1','c2','c3', 'c4')
    tree = ttk.Treeview(window, columns=columns, show='headings',height=52)
    # define headings
    tree.heading('c1', text='Numer Wiersza')
    tree.heading('c2', text='Numer Pracownika')
    tree.heading('c3', text='Data Rozpoczęcia Pracy')
    tree.heading('c4', text='Godzina Zakończenia Pracy')
    # add data to the treeview
    cur.execute("select * from wyjscie")
    rows = cur.fetchall()
    for row in rows:
        tree.insert('', tk.END, values=(row[0],row[1],row[2],row[3]))
    tree.grid(row=0, column=0, sticky='nsew')
    # add a scrollbar
    scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

def explore_work_time():
    window = tk.Tk()
    window.title('Obliczanie Czasu Pracy')
    window.geometry('1450x1000')
    # define columns
    columns = ('c1', 'c2', 'c3', 'c4', 'c5','c6')
    tree = ttk.Treeview(window, columns=columns, show='headings', height=52)
    # define headings
    tree.heading('c1', text='Numer Wiersza')
    tree.heading('c2', text='Numer Pracownika')
    tree.heading('c3', text='Data Rozpoczęcia Pracy')
    tree.heading('c4', text='Godzina Rozpoczęcia Pracy')
    tree.heading('c5', text='Godzina Zakończenia Pracy')
    tree.heading('c6', text='Całkowity Czas Pracy')
    # add data to the treeview
    con = sqlite3.connect(" overtime_db ")
    cur = con.cursor()
    cur.execute("select wejscie.id,wejscie.numer_pers,wejscie.dzień,godzina_rozpoczęcia,godzina_zakończenia,ROUND((JULIANDAY(godzina_zakończenia) - JULIANDAY(godzina_rozpoczęcia)) *1440 )as difference, wejscie.id from wejscie inner join wyjscie on wejscie.numer_pers= wyjscie.numer_pers")
    rows = cur.fetchall()
    for row in rows:
        tree.insert('', tk.END, values=(row[0], row[1], row[2], row[3], row[4],row[5]))
        tree.grid(row=0, column=0, sticky='nsew')
        # add a scrollbar
        scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')


def administratio_panel():
    window = tk.Tk()
    window.title('Całkowity czas pracy')
    window.geometry('1050x1000')
    # define columns
    columns = ('c1', 'c2', 'c3', 'c4', 'c5')
    tree = ttk.Treeview(window, columns=columns, show='headings', height=52)
    # define headings
    tree.heading('c1', text='Numer Pracownika')
    tree.heading('c2', text='Czas Pracy')
    tree.heading('c3', text='Ilość Dni')
    tree.heading('c4', text='Czas Pracy Wynikający z Etatu')
    tree.heading('c5', text='Całkowity Czas Pracy')
    # add data to the treeview
    con = sqlite3.connect(" overtime_db ")
    cur = con.cursor()
    cur.execute("select wejscie.numer_pers,sum(ROUND((JULIANDAY(godzina_zakończenia) - JULIANDAY(godzina_rozpoczęcia)) *1440 ))AS diff, count(wejscie.dzień), (count(wejscie.dzień)*480) as time_from_pr,sum(ROUND((JULIANDAY(godzina_zakończenia) - JULIANDAY(godzina_rozpoczęcia)) *1440 ))-(count(wejscie.dzień)*480) from wejscie inner join wyjscie on wejscie.numer_pers= wyjscie.numer_pers group by wejscie.numer_pers order by wejscie.numer_pers")
    rows = cur.fetchall()
    for row in rows:
        tree.insert('', tk.END, values=(row[0], row[1], row[2], row[3], row[4]))
        tree.grid(row=0, column=0, sticky='nsew')
        # add a scrollbar
        scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')


def narzedzia():
    windowq = tk.Tk()
    windowq.title('Całkowity czas pracy')
    windowq.geometry('750x150')
    Label(windowq,text="Narzędzia Służą Czyszczeniu Danych z Tabel Zachowaj Ostrożność",font=("arial",18),background='red',foreground='yellow').grid(row=1,column=0,pady=10,sticky='W')
    Label(windowq,text='Wyczyść Tabele Wejść',font=("arial",10),background='white',foreground='black').grid(row=2,column=0,pady=10,padx=10,sticky='W')
    Label(windowq, text='Wyczyść Tabele Wyjść', font=("arial", 10), background='white', foreground='black').grid(row=2,column=0,pady=10,sticky='E')
    Button(windowq,text="Wyczyść Tabelę Wejść",command=czysc_wejscie).grid(row=3,column=0,pady=10,padx=10,sticky='W')
    Button(windowq, text="Wyczyść Tabelę Wyjść",command=czysc_wyjscie).grid(row=3, column=0,pady=10,padx=10,sticky='E')




def czysc_wejscie():
    con = sqlite3.connect(" overtime_db ")
    cur = con.cursor()
    q=tk.messagebox.askyesno('Czyszczenie Tabeli',"Chcesz wyczyścić tabelę wejść?")
    if q ==1:
        cur.execute("delete from wejscie")
        con.commit()
    elif q==0:
        time.sleep(5)


def czysc_wyjscie():
    con = sqlite3.connect(" overtime_db ")
    cur = con.cursor()
    q=tk.messagebox.askyesno('Czyszczenie Tabeli',"Chcesz wyczyścić tabelę wyjść?")
    if q ==True:
        cur.execute("delete from wyjscie")
        con.commit()
    elif q==0:
        time.sleep(5)



menubar = Menu(window)
window.config(menu=menubar)
filemenu = Menu(menubar, tearoff = 0)
settingmenu = Menu(menubar, tearoff = 0)
viewmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(
    label="Zamknij",
    menu=filemenu)
menubar.add_cascade(
    label="Podgląd",
    menu=viewmenu)
menubar.add_cascade(
    label="Narzędzia",
    menu=settingmenu)


filemenu.add_command(label = "Wyjście",command=window.destroy)
viewmenu.add_command(label = "Uruchom Bazę Wejść",command=explore_entry)
viewmenu.add_command(label = "Uruchom Bazę Wyjść",command=expolre_exit)
viewmenu.add_command(label = "Wylicz Czas Pracy",command=explore_work_time)
settingmenu.add_command(label = "Uruchom Panel Administracyjny",command=administratio_panel)
settingmenu.add_command(label = "Uruchom Narzędzia Administracyjne",command=narzedzia)


window.mainloop()