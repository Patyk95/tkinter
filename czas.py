import sys
from tkinter import *
from time import strftime
from tkinter.ttk import *
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

cur.execute(
    "create table if not exists wejscie('id' integer primary key autoincrement,'numer_pers' not null,'dzień','godzina_rozpoczęcia','dz1','godzina_zak')")

#cur.execute("drop table wejscie")


def start():
    window = Tk()
    window.title("Czas pracy")
    window.geometry("450x450")
    window.config(background='black')

    czas = time.gmtime()
    w = calendar.timegm(czas)
    date_time = datetime.fromtimestamp(w)
    czas_to_date = date_time.strftime("%d-%m-%Y %H:%M:%S")



    def check_numer():
        if num_pers.get():
            start1()
        else:
            tk.messagebox.showerror('Numer Personalny Musi Być Podany', "Brak Numeru Praconika-Zacznij Ponownie")

    def start1():
        czas = time.gmtime()
        w = calendar.timegm(czas)
        date_time = datetime.fromtimestamp(w)
        data = date_time.strftime("%d-%m-%Y ")
        date_format_str = '%d-%m-%Y %H:%M:%S'
        start = datetime.strptime(czas_to_date, date_format_str)
        con = sqlite3.connect(" overtime_db ")
        cur = con.cursor()
        cur.execute("insert into wejscie ('numer_pers','dzień','godzina_rozpoczęcia','dz1','godzina_zak')values(:num,:dz,:godz,:dzi1,:godz_z)",
                    {
                        'num': num_pers.get(),
                        'dz': data,
                        'godz': start,
                        'dzi1':'empty',
                        'godz_z':'empty'
                    })
        num_pers.delete(0, END)
        messagebox.showinfo(title="Rozpoczęcie pracy", message='Dodano czas rozpoczęcia pracy')
        con.commit()
        window.destroy()



    num_pers = tk.Entry(window, font=('arial', 25),border=6)
    num_pers.grid(row=1, column=0, pady=10, padx=10)  # num_personalny
    num_personalny_label = Label(window, text='Wprowadź swój numer identyfikacyjny: ', font=("arial", 17),background='grey',border=6, foreground='black').grid(row=0, column=0,padx=20 ,pady=20)

    b1 = tk.Button(window, text="Rozpocznij pracę", command=check_numer, background='red',font=('Arial',25),height=3).grid(row=5, column=0, padx=20, pady=50)

    window.mainloop()



####################################

def stop():
    window = Tk()
    window.title("Czas pracy")
    window.geometry("450x450")
    window.config(background='black')

    czas = time.gmtime()
    w = calendar.timegm(czas)
    date_time = datetime.fromtimestamp(w)
    czas_to_date = date_time.strftime("%d-%m-%Y %H:%M:%S")


    def koniec():
            czas = time.gmtime()
            w = calendar.timegm(czas)
            date_time = datetime.fromtimestamp(w)
            data = date_time.strftime("%d-%m-%Y ")
            date_format_str = '%d-%m-%Y %H:%M:%S'
            end = datetime.strptime(czas_to_date, date_format_str)
            con = sqlite3.connect(" overtime_db ")
            cur = con.cursor()
            #try:
            cur.execute("update wejscie set 'dz1'=:dz,'godzina_zak'=:godz where numer_pers =:nump and id=:id1 ",
                            {
                                'nump': num_pers.get(),
                                'dz': data,
                                'godz': end,
                                'id1': id.get()

                            })
            #except sqlite3.OperationalError:
             #   tk.messagebox.showerror('Numer Personalny Musi Być Podany', "Brak Numeru Praconika-Zacznij Ponownie")
             #   window.destroy()
            con.commit()
            num_pers.delete(0, END)
            messagebox.showinfo(title="Zakończenie pracy", message='Dodano czas ukończenia pracy')
            window.destroy()




    def check_numer1():
        if num_pers.get():
            koniec()
        else:
            tk.messagebox.showerror('Numer Personalny Musi Być Podany', "Brak Numeru Praconika-Zacznij Ponownie")


    
    num_pers = tk.Entry(window, font=('arial', 25),border=6)
    num_pers.grid(row=1, column=0, pady=10, padx=10)  # num_personalny

    id = tk.Entry(window, font=('arial', 25),border=6)
    id.grid(row=3, column=0, pady=10, padx=10)  # num_personalny



    num_personalny_label = Label(window, text='Wprowadź swój numer identyfikacyjny: ', font=("arial", 17),background='grey',border=6, foreground='black').grid(row=0, column=0,padx=20 ,pady=20)
    id_label = Label(window, text='Wprowadź swój numer identyfikacyjny: ', font=("arial", 17),background='grey',border=6, foreground='black').grid(row=2, column=0,padx=20 ,pady=20)


    b1 = tk.Button(window, text="Zakończ pracę", command=check_numer1, background='red',font=('Arial',25),height=3).grid(row=4, column=0, padx=20, pady=15)



# creating an object of tkinter main menu


def czas():
        godzina = strftime('%H : %M : %S')
        lbl_godz.config(text="Aktualna godzina to: " + godzina)
        lbl_godz.after(1000, czas)


def data():
    dzien = strftime('%d - %m - %Y')
    lbl_dzien.config(text="Dziś jest: " + dzien)


def czysc_wejscie():
    con = sqlite3.connect(" overtime_db ")
    cur = con.cursor()
    q = tk.messagebox.askyesno('Czyszczenie Tabeli', "Chcesz wyczyścić tabelę wejść?")
    if q == 1:
        cur.execute("delete from wejscie")
        con.commit()
    elif q == 0:
        time.sleep(5)


def czysc_wyjscie():
    con = sqlite3.connect(" overtime_db ")
    cur = con.cursor()
    q = tk.messagebox.askyesno('Czyszczenie Tabeli', "Chcesz wyczyścić tabelę wyjść?")
    if q == True:
        cur.execute("delete from wyjscie")
        con.commit()
    elif q == 0:
        time.sleep(5)


def explore_entry():
    window = tk.Tk()
    window.title('Baza Wejść')
    window.geometry('1250x1000')
    # define columns
    columns = ('c1', 'c2', 'c3', 'c4','c5','c6')
    tree = ttk.Treeview(window, columns=columns, show='headings', height=52)
    # define headings
    tree.heading('c1', text='Numer Wiersza')
    tree.heading('c2', text='Numer Pracownika')
    tree.heading('c3', text='Data Rozpoczęcia')
    tree.heading('c4', text='Godzina Rozpoczęcia')
    tree.heading('c5', text='Dzień Zakończenia')
    tree.heading('c6', text='Godzina Zakończenia')


    # add data to the treeview
    cur.execute("select * from wejscie")
    rows = cur.fetchall()
    for row in rows:
        tree.insert('', tk.END, values=(row[0], row[1], row[2], row[3],row[4],row[5]))
    tree.grid(row=0, column=0, sticky='ne')
    # add a scrollbar
    scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')


def explore_work_time():
    window = tk.Tk()
    window.title('Obliczanie Czasu Pracy')
    window.geometry('1450x1000')
    # define columns
    columns = ('c1', 'c2', 'c3', 'c4', 'c5', 'c6')
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
    cur.execute(
        "select id,numer_pers,dzień,godzina_rozpoczęcia,godzina_zak,ROUND((JULIANDAY(godzina_zak) - JULIANDAY(godzina_rozpoczęcia)) *1440 )as difference from wejscie")
    rows = cur.fetchall()
    for row in rows:
        tree.insert('', tk.END, values=(row[0], row[1], row[2], row[3], row[4], row[5]))
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
    cur.execute(
        "select wejscie.numer_pers,sum(ROUND((JULIANDAY(godzina_zak) - JULIANDAY(godzina_rozpoczęcia)) *1440 ))AS diff,count(DISTINCT wejscie.dzień)as days, (count(DISTINCT wejscie.dzień)*480) as time_from_pr,sum(ROUND((JULIANDAY(godzina_zak) - JULIANDAY(godzina_rozpoczęcia)) *1440 ))-(count(DISTINCT wejscie.dzień)*480) from wejscie group by wejscie.numer_pers, wejscie.dzień order by wejscie.numer_pers")
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
    Label(windowq, text="Narzędzia Służą Czyszczeniu Danych z Tabel Zachowaj Ostrożność", font=("arial", 18),background='red', foreground='yellow').grid(row=1, column=0, pady=10, sticky='W')
    Label(windowq, text='Wyczyść Tabele Wejść', font=("arial", 10), background='white', foreground='black').grid(row=2, column=0,pady=10,padx=10,sticky='W')
    Label(windowq, text='Wyczyść Tabele Wyjść', font=("arial", 10), background='white', foreground='black').grid(row=2,column=0,pady=10,sticky='E')
    Button(windowq, text="Wyczyść Tabelę Wejść", command=czysc_wejscie).grid(row=3, column=0, pady=10, padx=10,sticky='W')
    Button(windowq, text="Wyczyść Tabelę Wyjść", command=czysc_wyjscie).grid(row=3, column=0, pady=10, padx=10,sticky='E')




window1 = Tk()
window1.title('System Obsługi Czasu')
window1.geometry('480x600')
window1.config(background='black')
B1 = tk.Button(window1, text='Rozpocznij Pracę', command=start,width=15, font=('Arial', 25), height=4, background='green',borderwidth=5)
B1.grid(row=2,column=0,pady=20,sticky='N')
B2 = tk.Button(window1, text='Zakończ Pracę', command=stop,width=15, font=('Arial', 25), height=4, background='yellow',borderwidth=5)
B2.grid(row=3,column=0,pady=20,sticky='N')
lbl_godz = Label(window1, font=('Arial', 20), background='white', foreground='black')  # display time
lbl_godz.grid(row=0, column=0, padx=20, pady=30)
czas()

lbl_dzien = Label(window1, font=('arial', 20), background='white', foreground='black')  # display date
lbl_dzien.grid(row=1, column=0)
data()

menubar = Menu(window1)
window1.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
settingmenu = Menu(menubar, tearoff=0)
viewmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(
    label="Zamknij",
    menu=filemenu)
menubar.add_cascade(
    label="Podgląd",
    menu=viewmenu)
menubar.add_cascade(
    label="Narzędzia",
    menu=settingmenu)

filemenu.add_command(label="Wyjście", command=window1.destroy)
viewmenu.add_command(label="Wyświetl Bazę Pracy", command=explore_entry)
viewmenu.add_command(label="Wylicz Czas Pracy", command=explore_work_time)
settingmenu.add_command(label="Uruchom Panel Administracyjny", command=administratio_panel)
settingmenu.add_command(label="Uruchom Narzędzia Administracyjne", command=narzedzia)
window1.mainloop()
