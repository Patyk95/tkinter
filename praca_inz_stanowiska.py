from tkinter import *
from time import strftime
import numpy as np
from xlsxwriter.workbook import Workbook
from tkinter import messagebox
import time
import datetime
import sqlite3
import calendar
from datetime import datetime
from tkinter import ttk
import tkinter as tk
from tkcalendar import DateEntry
con=sqlite3.connect('factory_db')
cur=con
#cur.execute("drop table wejscie")
#cur.execute('drop table status_produkcji')
#cur.execute("drop table status_produkcji")


''''
Czas Pracy
Czas Pracy
Czas Pracy
'''

def czas_pracy():
    # creating dbbms
    con = sqlite3.connect('factory_db')
    cur = con.cursor()
    cur.execute("create table if not exists wejscie(id integer primary key autoincrement,numer_pers not null,dzien,godzina_r,dzien1,godzina_z)")
    # cur.execute("drop table wyjscie")
    window = Tk()
    window.title("Czas pracy")
    window.geometry("550x450")
    window.configure(background='#b3b3b3')
    czas1 = time.gmtime()
    w = calendar.timegm(czas1)
    date_time = datetime.fromtimestamp(w)
    czas_to_date = date_time.strftime("%Y-%m-%d %H:%M:%S")

    def data():
        dzien = strftime('%Y - %m - %d')
        lbl_dzien.config(text="Jest: " + dzien)

    def check_numer():
        if num_pers.get():
            con = sqlite3.connect('factory_db')
            cur = con
            results = cur.execute('select * from pracownicy where numer_personalny=?', (num_pers.get(),))
            w1 = results.fetchall()
            if len(w1)>0:
                if b3.get():
                    start()
                else:
                    messagebox.showerror("Błąd Danych","Nie Podano Wartości")
                    window.destroy()
            else:
                messagebox.showerror("Błąd Danych","Podany Numer Personalny Nie Istnieje W Systemie")
                window.destroy()
        else:
            tk.messagebox.showerror('Błąd Danych', "Numer Personalny Musi Być Podany-Zacznij Ponownie")
            window.destroy()
    def check_numer1():
        if num_pers.get():
            con = sqlite3.connect('factory_db')
            cur = con
            results = cur.execute('select * from pracownicy where numer_personalny=?', (num_pers.get(),))
            w1 = results.fetchall()
            if len(w1) > 0:
                if b3.get():
                    koniec()
                else:
                    messagebox.showerror("Błąd Danych", "Nie Podano Wartości")
                    window.destroy()
            else:
                messagebox.showerror("Błąd Danych", "Podany Numer Personalny Nie Istnieje W Systemie")
                window.destroy()
            tk.messagebox.showerror('Błąd Danych', "Numer Personalny Musi Być Podany-Zacznij Ponownie")
            window.destroy()

    def start():
        time.gmtime()
        w = calendar.timegm(czas1)
        date_time = datetime.now().fromtimestamp(w)
        data = date_time.strftime("%Y-%m-%d ")
        date_format_str = '%Y-%m-%d %H:%M:%S'
        start = datetime.strptime(czas_to_date, date_format_str)
        con = sqlite3.connect('factory_db')
        cur = con
        e = 'empty'
        cur.execute(
            "insert into wejscie(numer_pers,dzien,godzina_r,dzien1,godzina_z)values(:num,:dz,:godz,:dz1,:godz2)",
            {
                'num': num_pers.get(),
                'dz': data,
                'godz': start,
                'dz1': e,
                'godz2': b3.get()
            })
        num_pers.delete(0, END)
        b3.delete(0, END)
        messagebox.showinfo(title="Informacja Systemowa", message='Dodano Czas Pracy ')
        con.commit()
        window.destroy()

    def koniec():
        czas = time.gmtime()
        w = calendar.timegm(czas)
        date_time = datetime.fromtimestamp(w)
        data1 = date_time.strftime("%Y-%m-%d ")
        date_format_str = '%Y-%m-%d %H:%M:%S'
        end = datetime.strptime(czas_to_date, date_format_str)
        con = sqlite3.connect('factory_db')
        cur = con.cursor()
        quer=("update wejscie set dzien1 = ?, godzina_z = ? where numer_pers = ? and godzina_z = ? ")
        dane=(data1,end,num_pers.get(),b3.get())
        cur.execute(quer,dane)
        con.commit()
        num_pers.delete(0, END)
        messagebox.showinfo(title="Informacja Systemowa", message='Dodano czas ukończenia pracy')
        window.destroy()
    lbl_dzien = Label(window, font=('arial', 30), background='white',foreground='black')  # data-wyświetlanie daty na gui
    lbl_dzien.grid(row=4, column=0)
    data()
    mystr = StringVar()
    mystr.set('Uzupełnij numer personalny w innym wypadku czas nie będzie naliczonoy')
    num_pers = Entry(window, font=('arial', 30))
    num_pers.grid(row=1, column=0, pady=10, padx=10)  # num_personalny
    num_personalny_label = Label(window, text='Wprowadź swój numer identyfikacyjny: ', font=("arial", 20),background='white', foreground='black')
    num_personalny_label.grid(row=0, column=0, pady=10)
    num_personalny_label1 = Label(window, text='Numer pracowniczy musi być podany by odnotować czas',font=("arial", 15), background='red', foreground='yellow')
    num_personalny_label1.grid(row=7, column=0,padx=10,pady=10)
    l1=Label(window,text='Podaj Wartość:',font=('arial',20),background='white')
    l1.grid(row=2,column=0,padx=10,pady=10)
    b3=Entry(window,font=('arial',20))
    b3.grid(row=3,column=0,padx=10,pady=10)
    b1 = Button(window, text="Rozpocznij pracę", command=check_numer, width=20)
    b1.grid(row=5, column=0, padx=20, pady=30,sticky='W')
    b2 = Button(window, text="Zakończ pracę", command=check_numer1, width=20)
    b2.grid(row=5, column=0, padx=20, pady=30,sticky='E')

    def explore_work_time():
        con = sqlite3.connect('factory_db')
        cur = con
        results = cur.execute("select id,numer_pers,dzien,godzina_r,godzina_z,ROUND((JULIANDAY(godzina_z) - JULIANDAY(godzina_r)) *1440 )as difference from wejscie where difference>1")
        d = results.fetchall()
        if len(d) > 0:
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
            rows=cur.execute("select id,numer_pers,dzien,godzina_r,godzina_z,ROUND((JULIANDAY(godzina_z) - JULIANDAY(godzina_r)) *1440 )as difference from wejscie where difference>1")
            for row in rows:
                tree.insert('', tk.END, values=(row[0], row[1], row[2], row[3], row[4], row[5]))
                tree.grid(row=0, column=0, sticky='nsew')
                # add a scrollbar
                scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
                tree.configure(yscroll=scrollbar.set)
                scrollbar.grid(row=0, column=1, sticky='ns')
        if len(d)<1:
            messagebox.showinfo('Informacja Systemowa','Baza Danych Nie Zawiera Odnotowanego Czasu')

    def narzedzia():
        windowq = tk.Tk()
        windowq.title('Całkowity czas pracy')
        windowq.geometry('750x150')
        windowq.configure(background='#b3b3b3')
        Label(windowq, text="Narzędzia Służą Czyszczeniu Danych z Tabel Zachowaj Ostrożność", font=("arial", 18),
              background='red', foreground='yellow').grid(row=1, column=0, pady=10, padx=10, sticky='N')
        Button(windowq, text="Wyczyść Tabelę Wejść",command=czysc_wejscie,font=('arial',30)).grid(row=3, column=0, pady=10, padx=10,sticky='N')
    def czysc_wejscie():
        con = sqlite3.connect('factory_db')
        cur = con.cursor()
        q = tk.messagebox.askyesno('Informacja Systemowa', "Chcesz wyczyścić tabelę wejść?")
        if q == 1:
            cur.execute("delete from wejscie")
            con.commit()
        elif q == 0:
            time.sleep(5)

    def explore_table():
        con = sqlite3.connect('factory_db')
        cur = con
        results = cur.execute('select * from wejscie')
        d = results.fetchall()
        if len(d) > 0:
            window=Tk()
            window.geometry('1450x850')
            window.configure(background='#b3b3b3')
            columns = ('c1', 'c2', 'c3', 'c4', 'c5','c6')
            tree = tk.ttk.Treeview(window, columns=columns, show='headings', height=52)
            # define headings
            tree.heading('c1', text='Id')
            tree.heading('c2', text='Numer Personalny')
            tree.heading('c3', text='Dzień')
            tree.heading('c4', text='Godzina Rozpoczęcia Pracy')
            tree.heading('c5', text='Dzień Zakończenia Pracy')
            tree.heading('c6', text='Godzina Zakończenia Pracy')
            # add data to the treeview
            con = sqlite3.connect('factory_db')
            cur = con
            for row in cur.execute('select * from wejscie'):
                tree.insert('', tk.END, values=(row[0], row[1], row[2], row[3], row[4],row[5]))
                tree.grid(row=0, column=0, sticky='n')
                # add a scrollbar
                scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
                tree.configure(yscroll=scrollbar.set)
                scrollbar.grid(row=0, column=1, sticky='ns')
                con.commit()
        if len(d)<1:
            messagebox.showinfo('Informacja Systemowa','Baza Danych jest Pusta')


    def pasword():
        def f1():
            if bb7.get() == c1:
                narzedzia()
                window1.destroy()
                window.iconify()
            else:
                messagebox.showinfo('Błąd Danych', 'Hasło Nie Jest Poprawne')
                window1.destroy()
        window1 = Tk()
        window1.geometry('450x300')
        window1.title('Weryfikacja Uprawnień')
        window1.configure(background='#b3b3b3')
        ll = Label(window1, text='Podaj Hasło', font=('arial', 25),background='white')
        ll.grid(row=1, column=1, sticky='N', padx=20, pady=20)
        c1 = 'admin1'
        bb7 = Entry(window1, font=('arial', 25),show='*')
        bb7.grid(row=2, column=1, sticky='N', padx=20, pady=20)
        bb2 = Button(window1, text='Wejdź', command=f1)
        bb2.grid(row=3, column=1, sticky='N', padx=20, pady=20)

    menubar = Menu(window)
    window.config(menu=menubar)
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
    filemenu.add_command(label="Wyjście", command=window.destroy)
    viewmenu.add_command(label="Wylicz Czas Pracy", command=explore_work_time)
    viewmenu.add_command(label="Podgląd Tabeli", command=explore_table)
    settingmenu.add_command(label="Uruchom Narzędzia Administracyjne", command=pasword)
'''
PRZEJSICE NA MODUŁ KADR - NUMERY PERSONALNE ORAZ PRAWOCOWNICY
PRZEJSICE NA MODUŁ KADR - NUMERY PERSONALNE ORAZ PRAWOCOWNICY
PRZEJSICE NA MODUŁ KADR - NUMERY PERSONALNE ORAZ PRAWOCOWNICY
'''
def karta_pers():
    window = Tk()
    window.title('System Zarządzania Personelem')
    window.config(background='#b3b3b3')
    window.state('zoomed')

    # creating Databases
    con = sqlite3.connect('factory_db')
    cur = con
    cur.execute(
        'create table if not exists pracownicy (id integer primary key autoincrement, imie, nazwisko, numer_telefonu,numer_personalny)')
    # cur.execute('drop table pracownicy')
    cur.execute(
        'create table if not exists numery_personalne (id integer primary key autoincrement,numer_personalny,nazwa_dzialu,czas_pracy_z_etatu,pensja_zasadnicza)')
    # cur.execute('drop table numery_personalne')
    def save():
        if b1.get() and b2.get() and b3.get() and b4.get() and b5.get() and b6.get():
            con = sqlite3.connect('factory_db')
            cur = con
            cur.execute(
                'insert into pracownicy (imie,nazwisko,numer_telefonu,numer_personalny) values(:imie,:nazwisko,:numer_telefonu,:numer_personalny)',
                {
                    'imie': b1.get(),
                    'nazwisko': b2.get(),
                    'numer_telefonu': b3.get(),
                    'numer_personalny': b4.get()
                })
            con.commit()
            cur.execute(
                'insert into numery_personalne (numer_personalny,nazwa_dzialu, czas_pracy_z_etatu,pensja_zasadnicza)values(:numer_personalny,:nazwa_dzialu,:czas_pracy_z_etatu,:pensja_zasadnicza)',
                {
                    'numer_personalny': b4.get(),
                    'nazwa_dzialu': b5.get(),
                    'czas_pracy_z_etatu': b6.get(),
                    'pensja_zasadnicza': b7.get()
                })
            con.commit()
            b1.delete(0, END)
            b2.delete(0, END)
            b3.delete(0, END)
            b4.delete(0, END)
            b5.delete(0, END)
            b6.delete(0, END)
            b7.delete(0, END)
        else:
            tk.messagebox.showwarning('Błąd Danych', 'Brakuje Jednego Z Wymaganych Pól')

    def checking():
        con = sqlite3.connect('factory_db')
        cur = con
        results = cur.execute("SELECT * from pracownicy WHERE numer_personalny= :numer_personalny", {
            'numer_personalny': b4.get()
        })
        if results.fetchall():
            w = tk.messagebox.askquestion('Informacja Systemowa',
                                          'Wpis Dla Podanego Pracownika Już Istnieje-Czy Chcesz Go Nadpisać?')
            if w == 'yes':
                cur.execute(
                    'update pracownicy set imie = :imie,nazwisko = :nazwisko,numer_telefonu = :numer_telefonu,numer_personalny = :numer_personalny where numer_personalny = :numer_personalny',
                    {
                        'imie': b1.get(),
                        'nazwisko': b2.get(),
                        'numer_telefonu': b3.get(),
                        'numer_personalny': b4.get()
                    })
                con.commit()
                cur.execute(
                    'update numery_personalne set numer_personalny = :numer_personalny,nazwa_dzialu = :nazwa_dzialu,czas_pracy_z_etatu = :czas_pracy_z_etatu,pensja_zasadnicza = :pensja_zasadnicza where numer_personalny = :numer_personalny',
                    {
                        'numer_personalny': b4.get(),
                        'nazwa_dzialu': b5.get(),
                        'czas_pracy_z_etatu': b6.get(),
                        'pensja_zasadnicza': b7.get()
                    })
                con.commit()
                tk.messagebox.showinfo('Informacja', 'Zmainy Zostały Zapisane')
                b1.delete(0, END)
                b2.delete(0, END)
                b3.delete(0, END)
                b4.delete(0, END)
                b5.delete(0, END)
                b6.delete(0, END)

            if w == 'no':
                tk.messagebox.showinfo('Informacja Systemowa', 'Zmiany Zostały Odrzucone')
        else:
            messagebox.showinfo('Informacja Systemowa', 'Proszę Utworzyć Wpis')

    def veryfication():
        if b1.get():
            if b2.get():
                if b3.get():
                    if b4.get():
                        if b5.get():
                            if b6.get():
                                if b7.get():
                                    tk.messagebox.showinfo('OK', 'Wszystkie Parametry Zostały Przypisane Poprawnie')
                                    checking()
                                else:
                                    tk.messagebox.showerror('Error', 'Pensja Zasadnicza Musi Zostać Ustalona')
                            else:
                                tk.messagebox.showerror('Error', 'Czas Pracy Wyrażony w Godzinach Musi Być Podany')
                        else:
                            tk.messagebox.showerror('Error', 'Nazwa Struktury Musi Być Zaewidencjonowana')
                    else:
                        tk.messagebox.showerror('Error', 'Numer Personalny Pracownika Musi Być Przypisany')
                else:
                    tk.messagebox.showerror('Error', 'Numer Telefonu Pracownika Musi Być Podany')
            else:
                tk.messagebox.showerror('Error', 'Nazwisko Pracownika Musi Być Podane')
        else:
            tk.messagebox.showerror('Error', 'Imię Pracownika Musi Być Podane')

    def display_pracownicy():
        window = tk.Tk()
        window.title('Dane Pracowników')
        window.geometry('1050x800')
        window.configure(background='#b3b3b3')
        # define columns
        columns = ('c1', 'c2', 'c3', 'c4', 'c5')
        tree = tk.ttk.Treeview(window, columns=columns, show='headings', height=52)
        # define headings
        tree.heading('c1', text='Id')
        tree.heading('c2', text='Imie Pracownika')
        tree.heading('c3', text='Nazwisko Pracownika')
        tree.heading('c4', text='Numer Telefonu')
        tree.heading('c5', text='Numer Personalny')

        # add data to the treeview
        con = sqlite3.connect('factory_db')
        cur = con
        for row in cur.execute('select id,imie, nazwisko, numer_telefonu,numer_personalny from pracownicy'):
            tree.insert('', tk.END, values=(row[0], row[1], row[2], row[3], row[4]))
            tree.grid(row=0, column=0, sticky='n')
            # add a scrollbar
            scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=1, sticky='ns')
            con.commit()

    def display_numery_pers():
        window = tk.Tk()
        window.title('Numery Personalne')
        window.geometry('1050x800')
        window.configure(background='#b3b3b3')
        # define columns
        columns = ('c1', 'c2', 'c3', 'c4', 'c5')
        tree = tk.ttk.Treeview(window, columns=columns, show='headings', height=52)
        # define headings
        tree.heading('c1', text='Id')
        tree.heading('c2', text='Numer Personalny')
        tree.heading('c3', text='Nazwa Działu')
        tree.heading('c4', text='Wymiar Czasu Pracy')
        tree.heading('c5', text='Pensja Zasadnicza')

        # add data to the treeview
        con = sqlite3.connect('factory_db')
        cur = con
        for row in cur.execute(
                'select id,numer_personalny,nazwa_dzialu,czas_pracy_z_etatu,pensja_zasadnicza from numery_personalne'):
            tree.insert('', tk.END, values=(row[0], row[1], row[2], row[3], row[4]))
            tree.grid(row=0, column=0, sticky='NE')
            # add a scrollbar
            scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=1, sticky='ns')
            con.commit()

    def to_excel():
        workbook = Workbook('Zestawienie_Pracowników.xlsx')
        worksheet = workbook.add_worksheet('Dane Pracowników')
        con = sqlite3.connect('factory_db')
        cur = con
        mysel = cur.execute("select * from pracownicy")
        for i, row in enumerate(mysel):
            for j, value in enumerate(row):
                worksheet.write(i, j, row[j])
        worksheet = workbook.add_worksheet('Weryfikacja Numerów')
        mysel1 = cur.execute("select * from numery_personalne")
        for i, row in enumerate(mysel1):
            for j, value in enumerate(row):
                worksheet.write(i, j, row[j])
        workbook.close()
        window.destroy()

    def to_upper(*args):
        var.set(var.get().upper())
        var1.set(var1.get().upper())
        var2.set(var2.get().upper())
        var3.set(var3.get().upper())
        var4.set(var4.get().upper())
        var5.set(var5.get().upper())
        var6.set(var6.get().upper())
    def pasword():
        def f1():
            if bb7.get() == c1:
                q = tk.messagebox.askyesno('Informacja Systemowa', "Chcesz Wyczyścić Tabelę Pracownicy?")
                if q == 1:
                    cur.execute("delete from pracownicy")
                    con.commit()
                    messagebox.showinfo('Informacja Systemowa', 'Baza Pracowników Została Wyczyszczona')
                    window1.title('Weryfikacja Uprawnień')
                    window.destroy()
                elif q == 0:
                    time.sleep(5)
                    messagebox.showinfo('Informacja Systemowa', 'Działanie Zostało Przerwane')
                    window1.destroy()
                    window.destroy()
            else:
                messagebox.showinfo('Błąd Danych', 'Hasło Nie Jest Poprawne')

        window1 = Tk()
        window1.geometry('450x300')
        window1.title('Weryfikacja Uprawnień')
        window1.configure(background='#b3b3b3')
        ll = Label(window1, text='Podaj Hasło', font=('arial', 25),background='white')
        ll.grid(row=1, column=1, sticky='N', padx=20, pady=20)
        c1 = 'admin1'
        bb7 = Entry(window1, font=('arial', 25),show='*')
        bb7.grid(row=2, column=1, sticky='N', padx=20, pady=20)
        bb2 = Button(window1, text='Wejdź', command=f1)
        bb2.grid(row=3, column=1, sticky='N', padx=20, pady=20)

    def pasword2():
        def f1():
            if bb7.get() == c1:
                q = tk.messagebox.askyesno('Informacja Systemowa', "Chcesz Wyczyścić Tabelę Numery Personalne?")
                if q == 1:
                    cur.execute("delete from numery_personalne")
                    con.commit()
                    window1.title('Weryfikacja Uprawnień')
                    messagebox.showinfo('Informacja Systemowa', 'Baza Została Wyczyszczona')
                    window.destroy()
                    window1.destroy()

                elif q == 0:
                    time.sleep(5)
                    window.destroy()
                    window1.destroy()
                    messagebox.showinfo('Informacja Systemowa', 'Działanie Zostało Przerwane')
            else:
                messagebox.showinfo('Błąd Danych', 'Hasło Nie Jest Poprawne')

        window1 = Tk()
        window1.geometry('450x300')
        window1.title('Weryfikacja Uprawnień')
        window1.configure(background='#b3b3b3')
        ll = Label(window1, text='Podaj Hasło', font=('arial', 25),background='white')
        ll.grid(row=1, column=1, sticky='N', padx=20, pady=20)
        c1 = 'admin1'
        bb7 = Entry(window1, font=('arial', 25),show='*')
        bb7.grid(row=2, column=1, sticky='N', padx=20, pady=20)
        bb2 = Button(window1, text='Wejdź', command=f1)
        bb2.grid(row=3, column=1, sticky='N', padx=20, pady=20)

    def pasword3():
        def f1():
            if bb7.get() == c1:
                con = sqlite3.connect('factory_db')
                cur = con
                results = cur.execute("select * from wejscie")
                d = results.fetchall()
                if len(d) > 0:
                    dt = cal.get_date()
                    str_dt4 = dt.strftime("%Y-%m-%d")
                    n = str_dt4
                    dzis = datetime.today()
                    dz1 = dzis.strftime("%Y-%m-%d")
                    k = np.busday_count(n, dz1)
                    k1=k*60
                    window1.destroy()
                    window = tk.Tk()
                    window.title('Okresowy Czasu Pracy')
                    window.geometry('1450x1000')
                    # define columns
                    columns = ('c1', 'c2', 'c3','c4')
                    tree = ttk.Treeview(window, columns=columns, show='headings', height=52)
                    # define headings
                    tree.heading('c1', text='Numer Wiersza')
                    tree.heading('c2', text='Numer Pracownika')
                    tree.heading('c3', text='Całkowity Czas Pracy')
                    tree.heading('c4', text='Całkowity Czas Pracy Wynikający Z Etatu')
                    # add data to the treeview
                    rows = cur.execute(
                    "select wejscie.id,numer_pers,SUM(ROUND((JULIANDAY(godzina_z) - JULIANDAY(godzina_r)) *1440 )) as dif,czas_pracy_z_etatu *60 from wejscie inner join numery_personalne on wejscie.numer_pers = numery_personalne.numer_personalny where dzien > :d1 group by numer_pers having dif >1 order by wejscie.id",{
                        'd1':str_dt4,
                        })
                    for row in rows:
                        tree.insert('', tk.END, values=(row[0], row[1], row[2],row[3]))
                        tree.grid(row=0, column=0, sticky='nsew')
                        # add a scrollbar
                        scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
                        tree.configure(yscroll=scrollbar.set)
                        scrollbar.grid(row=0, column=1, sticky='ns')
                if len(d) < 1:
                    window1.destroy()
                    messagebox.showinfo('Informacja Systemowa', 'Baza Danych Nie Zawiera Odnotowanego Czasu')
        window1 = Tk()
        window1.geometry('450x300')
        window1.title('Weryfikacja Uprawnień')
        window1.configure(background='#b3b3b3')
        ll = Label(window1, text='Podaj Hasło', font=('arial', 25),background='white')
        ll.grid(row=1, column=1, sticky='N', padx=20, pady=20)
        c1 = 'admin1'
        bb7 = Entry(window1, font=('arial', 25),show='*')
        bb7.grid(row=2, column=1, sticky='N', padx=20, pady=20)
        bb2 = Button(window1, text='Wejdź',font=('arial',15),command=f1)
        bb2.grid(row=3,column=1,padx=10,pady=10)
        cal = DateEntry(window1, selectmode='day', date_pattern='yyyy-MM-dd',font=('arial',15))
        cal.grid(row=4, column=1, padx=15, pady=10,sticky='W')

    var = tk.StringVar(window)
    var1 = tk.StringVar(window)
    var2 = tk.StringVar(window)
    var3 = tk.StringVar(window)
    var4 = tk.StringVar(window)
    var5 = tk.StringVar(window)
    var6 = tk.StringVar(window)

    l_tit = Label(window, text='Zakładanie Karty Pracownika', font=('arial', 40), background='white')
    l_tit.grid(row=0, column=0, pady=20, columnspan=1, sticky='N')
    l1 = Label(window, text='Podaj Imię Pracownika:', font=('arail', 20), background='white')
    l1.grid(row=1, column=0, pady=10, padx=10, sticky='W')
    b1 = Entry(window, textvariable=var, font=('arail', 25))
    b1.grid(row=1, column=2, padx=10, pady=8, sticky='W')
    l2 = Label(window, text='Podaj Nazwisko Pracownika:', font=('arial', 20), background='white')
    l2.grid(row=2, column=0, pady=10, padx=10, sticky='W')
    b2 = Entry(window, textvariable=var1, font=('arail', 25))
    b2.grid(row=2, column=2, padx=10, pady=8, sticky='N')
    l3 = Label(window, text='Podaj Numer Telefonu Pracownika:', font=('arial', 20), background='white')
    l3.grid(row=3, column=0, pady=10, padx=10, sticky='W')
    b3 = Entry(window, textvariable=var2, font=('arail', 25))
    b3.grid(row=3, column=2, padx=10, pady=8, sticky='N')
    l4 = Label(window, text='Nadaj Numer Personalny Pracownikowi:', font=('arial', 20), background='white')
    l4.grid(row=4, column=0, pady=10, padx=10, sticky='W')
    b4 = Entry(window, textvariable=var3, font=('arail', 25))
    b4.grid(row=4, column=2, padx=10, pady=8, sticky='N')
    l5 = Label(window, text='Podaj Nazwę Struktury Organizacyjnej:', font=('arial', 20), background='white')
    l5.grid(row=5, column=0, pady=10, padx=10, sticky='W')
    b5 = Entry(window, textvariable=var4, font=('arail', 25))
    b5.grid(row=5, column=2, padx=10, pady=8, sticky='N')
    l6 = Label(window, text='Podaj Czas Pracy Wynikający Z Formy Zatrudnienia:', font=('arial', 20), background='white')
    l6.grid(row=6, column=0, pady=10, padx=10, sticky='W')
    b6 = Entry(window, textvariable=var5, font=('arail', 25))
    b6.grid(row=6, column=2, padx=10, pady=8, sticky='N')
    l7 = Label(window, text='Ustal Pensję Zasadniczą Pracownika:', font=('arial', 20), background='white')
    l7.grid(row=7, column=0, pady=10, padx=10, sticky='W')
    b7 = Entry(window, textvariable=var6, font=('arail', 25))
    b7.grid(row=7, column=2, padx=10, pady=8, sticky='N')
    b8 = Button(window, text='SPRAWDŹ', command=veryfication, font=('arial', 30), background='#3399ff')
    b8.grid(row=8, column=0, padx=10, pady=50, sticky='N')
    b9 = Button(window, text='ZATWIERDŹ', command=save, font=('arial', 30), background='Green')
    b9.grid(row=8, column=2, padx=10, pady=50, sticky='N')
    b10 = Button(window, text='Sprawdź Tabelę Pracowników', command=display_pracownicy, font=('arial', 15),
                 background='#99cc00')
    b10.grid(row=9, column=2, padx=10, pady=10, sticky='N')
    b11 = Button(window, text='Sprawdź Tablę Numerów Personalnych', command=display_numery_pers, font=('arial', 15),
                 background='#99cc00')
    b11.grid(row=9, column=0, padx=10, pady=10, sticky='N')
    b12 = Button(window, text='Pobierz Zestawienie Pracowników', command=to_excel, font=('arial', 15),
                 background='#b30000')
    b12.grid(row=9, column=3, columnspan=2, padx=10, pady=10, sticky='N')
    var.trace_add('write', to_upper)
    var1.trace_add('write', to_upper)
    var2.trace_add('write', to_upper)
    var3.trace_add('write', to_upper)
    var4.trace_add('write', to_upper)
    var5.trace_add('write', to_upper)
    var6.trace_add('write', to_upper)
    menubar = Menu(window)
    window.config(menu=menubar)
    filemenu = Menu(menubar, tearoff=0)
    settingmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(
        label="Zamknij",
        menu=filemenu)
    menubar.add_cascade(
        label="Narzędzia Administracyje",
        menu=settingmenu)
    filemenu.add_command(label="Wyjście", command=window.quit)
    settingmenu.add_command(label="Czyszczenie Tabeli Pracowników",command=pasword)
    settingmenu.add_command(label="Czyszczenie Tabeli Numery Personalne",command=pasword2)
    settingmenu.add_command(label="Rozliczanie Czasu Pracy",command=pasword3)

'''
PRZEŁĄCZENIE SIĘ NA RAPORTOWANIE PRODUKCJI
PRZEŁĄCZENIE SIĘ NA RAPORTOWANIE PRODUKCJI
PRZEŁĄCZENIE SIĘ NA RAPORTOWANIE PRODUKCJI
'''
def produkcja():
    # connection and database
    con = sqlite3.connect('factory_db')
    cur = con
    cur.execute(
        "create table  if not exists status_produkcji('id' integer primary key autoincrement,product not null, qty,qty1,date,employee,additional_info,shift)")
    # Gui
    window = Tk()
    window.title('System Weryfikacji Produkcji')
    window.state('zoomed')
    window.configure(background='#b3b3b3')

    dkx = datetime.today()
    dkx1 = dkx.strftime('%Y-%m-%d,%H :%M :%S')
    dkx2 = dkx.strftime('%Y-%m-%d')

    def confirmation():
        con = sqlite3.connect('factory_db')
        cur = con
        cur.execute(
            "insert into status_produkcji(product,shift,qty,qty1,date,employee,additional_info) values(:product,:shift,:qty,:qty1,:date,:employee,:additional_info)",
            {
                'product': b1.get(),
                'shift': b8.get(),
                'qty': b2.get(),
                'qty1':b9.get(),
                'date': dkx2,
                'employee': b3.get(),
                'additional_info': b4.get()
            })
        con.commit()
        messagebox.showinfo('Informacja Systemowa','Dane Zostały Zapisane W Bazie')
        b1.delete(0, END)
        b2.delete(0, END)
        b3.delete(0, END)
        b4.delete(0, END)
        b8.delete(0, END)
        b9.delete(0, END)

    def reject():
        b1.delete(0, END)
        b2.delete(0, END)
        b3.delete(0, END)
        b4.delete(0, END)
        b8.delete(0, END)
        b9.delete(0,END)
        messagebox.showinfo('Informacja Systemowa', 'Dane Zostały Odrzucone - Wpis Nie Został Utworzony')
    def check_if_empty():
        if b1.get():
                con=sqlite3.connect('factory_db')
                cur=con
                results = cur.execute('select * from material where numer_materialu=?', (b1.get(),))
                w=results.fetchall()
                if len(w)>=1:
                    if b2.get():
                        if b3.get():
                            con = sqlite3.connect('factory_db')
                            cur = con
                            results = cur.execute('select * from pracownicy where numer_personalny=?', (b3.get(),))
                            w1 = results.fetchall()
                            if len(w1) >= 1:
                                if b8.get():
                                    if b8.get()< '4':
                                        if b9.get():
                                            confirmation()
                                        else:
                                            tk.messagebox.showerror("Błąd danych","Liczba Części Uszkodzonych Nie Może Być Pusta")
                                    else:
                                        tk.messagebox.showerror("Błąd danych","Numer Zmiany Poza Zakresem (1-3)")
                                else: tk.messagebox.showerror("Błąd danych", "Nie Podano Numeru Zmiany Lub Podano Niepoprawną Wartość")
                            else:messagebox.showerror("Błąd Danych","Taki Numer Personalny Nie Istnieje W Systemie")
                        else:tk.messagebox.showerror("Błąd danych","Nie Podano Numeru Personalnego")
                else:tk.messagebox.showerror("Błąd Danych","Podany Materiał Nie Istnieje W Systemie")
        else:messagebox.showerror('Błąd Danych',"Podaj Numer Materiału ")

    def show_my():
        if b3.get():
            show_my_results()
        else:
            tk.messagebox.showerror('Błąd Danych', 'Numer Personalny Musi Zostać Podany')

    def show_my_results():
        con=sqlite3.connect('factory_db')
        cur=con
        results = cur.execute('select * from pracownicy where numer_personalny=?', (b3.get(),))
        w1 = results.fetchall()
        if len(w1) > 0:
            con = sqlite3.connect('factory_db')
            w = cur.execute(
                'select id,date,shift,product,qty,qty1,employee,additional_info from status_produkcji where employee = :employee',
                {
                    'employee': b3.get()})
            d = w.fetchall()
            if len(d) > 0:
                window = tk.Tk()
                window.title('Moje Rezultaty')
                window.geometry('1450x800')
                window.configure(background='#b3b3b3')
                # define columns
                columns = ('c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7','c8')
                tree = ttk.Treeview(window, columns=columns, show='headings', height=52)
                # define headings
                tree.heading('c1', text='ID')
                tree.heading('c2', text='Data')
                tree.heading('c3', text='Numer Zmiany')
                tree.heading('c4', text='Numer Części')
                tree.heading('c5', text='Ilość')
                tree.heading('c6', text='Ilość Częsci Uszkodzonych/NIOK')
                tree.heading('c7', text='Numer Personalny')
                tree.heading('c8', text='Komentarz')
                #add data to the treeview
                for row in cur.execute(
                    'select id,date,shift,product,qty,qty1,employee,additional_info from status_produkcji where employee = :employee',
                    {
                        'employee': b3.get()
                    }):
                    tree.insert('', tk.END, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7]))
                    tree.grid(row=0, column=0, sticky='nsew')
                    # add a scrollbar
                    scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
                    tree.configure(yscroll=scrollbar.set)
                    scrollbar.grid(row=0, column=1, sticky='ns')
                    con.commit()
            if len(d)<1:
                messagebox.showinfo('Informacja Systemowa','Dla Podanego Numeru Personalnego Nie Odnotowano Jeszcze Rejesteru')
        else:
            messagebox.showerror("Błąd Danych", "Podany Numer Personalny Nie Istnieje W Systemie")

    def export_to_excel():
        workbook = Workbook('archiwum.xlsx')
        worksheet = workbook.add_worksheet()
        con = sqlite3.connect('factory_db')
        c = con.cursor()
        con.execute("select * from status_produkcji")
        mysel = c.execute("select * from status_produkcji")
        for i, row in enumerate(mysel):
            for j, value in enumerate(row):
                worksheet.write(i, j, row[j])
        workbook.close()
        window.destroy()

    def pasword():
        def f1():
            if bb7.get() == c1:
                q = tk.messagebox.askyesno('Informacja Systemowa', "Chcesz Wyczyścić Bazę Status Produckji?")
                if q == 1:
                    cur.execute("delete from status_produkcji")
                    con.commit()
                    messagebox.showinfo('Informacja Systemowa', 'Baza Została Wyczyszczona')
                    window.destroy()
                    window1.destroy()

                elif q == 0:
                    time.sleep(5)
                    messagebox.showinfo('Informacja Systemowa', 'Działanie Zostało Przerwane')
                    window1.destroy()
                    window.destroy()
            else:
                messagebox.showinfo('Błąd Danych', 'Hasło Nie Jest Poprawne')

        window1 = Tk()
        window1.geometry('450x300')
        window1.title('Weryfikacja Uprawnień')
        window1.configure(background='#b3b3b3')
        ll = Label(window1, text='Podaj Hasło', font=('arial', 25),background='white')
        ll.grid(row=1, column=1, sticky='N', padx=20, pady=20)
        c1 = 'admin1'
        bb7 = Entry(window1, font=('arial', 25),show='*')
        bb7.grid(row=2, column=1, sticky='N', padx=20, pady=20)
        bb2 = Button(window1, text='Wejdź', command=f1)
        bb2.grid(row=3, column=1, sticky='N', padx=20, pady=20)

    def pasword2():
        def f1():
            if bb7.get() == c1:
                window1.destroy()
                window.geometry('1450x800')
                # define columns
                columns = ('c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8')
                tree = ttk.Treeview(window, columns=columns, show='headings', height=52)
                # define headings
                tree.heading('c1', text='ID')
                tree.heading('c2', text='Data')
                tree.heading('c3', text='Numer Zmiany')
                tree.heading('c4', text='Numer Części')
                tree.heading('c5', text='Ilość')
                tree.heading('c6', text='Ilość Częsci Uszkodzonych/NIOK')
                tree.heading('c7', text='Numer Personalny')
                tree.heading('c8', text='Komentarz')
                # add data to the treeview
                con = sqlite3.connect('factory_db')
                cur = con
                results=cur.execute('select * from status_produkcji')
                w=results.fetchall()
                if len(w)>0:
                    for row in cur.execute('select id,date,shift,product,qty,qty1,employee,additional_info from status_produkcji'):
                        tree.insert('', tk.END, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
                        tree.grid(row=0, column=0, sticky='nsew')
                        # add a scrollbar
                        scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
                        tree.configure(yscroll=scrollbar.set)
                        scrollbar.grid(row=0, column=1, sticky='ns')
                        con.commit()
                else:
                    messagebox.showinfo('Informacaj Systemowa','Baza Danych Jest Czysta')
            else:
                messagebox.showinfo('Błąd Danych', 'Hasło Nie Jest Poprawne')
        window1 = Tk()
        window1.geometry('450x300')
        window1.title('Weryfikacja Uprawnień')
        window1.configure(background='#b3b3b3')
        ll = Label(window1, text='Podaj Hasło', font=('arial', 25),background='white')
        ll.grid(row=1, column=1, sticky='N', padx=20, pady=20)
        c1 = 'admin1'
        bb7 = Entry(window1, font=('arial', 25),show='*')
        bb7.grid(row=2, column=1, sticky='N', padx=20, pady=20)
        bb2 = Button(window1, text='Wejdź', command=f1)
        bb2.grid(row=3, column=1, sticky='N', padx=20, pady=20)
    text = Text(window, height=20, width=40)

    def to_upper(*args):
        var.set(var.get().upper())
        var1.set(var1.get().upper())
        var2.set(var2.get().upper())

    var = tk.StringVar(window)
    var1 = tk.StringVar(window)
    var2 = tk.StringVar(window)
    l1 = Label(window, text='Podaj Produkowany Artykuł:', font=("arial", 20), background='white')
    l1.grid(padx=20, pady=20, row=1, column=1,sticky='W')
    b1 = Entry(window, width=25, font=('arial', 20),textvariable=var)
    b1.grid(padx=20, pady=20, column=2, row=1,sticky='W')
    # Produced qty
    l2 = Label(window, text='Odnotuj Wyprodukowane Ilośći:', font=("arial", 20), background='white')
    l2.grid(padx=20, pady=20, row=2, column=1,sticky='W')
    b2 = Entry(window, width=25, font=('arial', 20),textvariable=var1)
    b2.grid(padx=20, pady=20, column=2, row=2)
    # Worker details
    l3 = Label(window, text='Podaj Numer Personalny:', font=("arial", 20), background='white')
    l3.grid(padx=20, pady=20, row=4, column=1,sticky='W')
    b3 = Entry(window, width=25, font=('arial', 20))
    b3.grid(padx=20, pady=20, row=4, column=2)
    l4 = Label(window, text='Podaj Informację Dodatkowe [Opcjonalnie]:', font=("arial", 20), background='white')
    l4.grid(padx=20, pady=20, row=5, column=1,sticky='W')
    b4 = Entry(window, width=25, font=('arial', 20),textvariable=var2)
    b4.grid(padx=20, pady=20, row=5, column=2)
    b5 = Button(window, text="Potwierdź I Dodaj", command=check_if_empty, font=("arial", 20), background="green")
    b5.grid(row=7, column=1)
    b6 = Button(window, text="Odrzuć", command=reject, font=("arial", 20), background="red")
    b6.grid(row=7, column=2, pady=25)
    b7 = Button(window, text="Pokaż Swoje Rezultaty", command=show_my, font=("arial", 20), background="Orange")
    b7.grid(row=8, column=2)
    b10 = Button(window, text="Exportujd Do Excela", command=export_to_excel, font=("arial", 20), background="Blue")
    b10.grid(row=8, column=1)
    b8 = Entry(window, font=('arial', 20), width=25)
    b8.grid(row=6, column=2, pady=15)
    l8 = Label(window, text="Podaj Numer Zmiany:", font=('arial', 20), bg='white')
    l8.grid(row=6, column=1,padx=20,pady=20,sticky='W')
    l9 = Label(window, text="Podaj Ilość Części Uszkodzonych:", font=('arial', 20), bg='white')
    l9.grid(row=3, column=1,padx=20,pady=20,sticky='W')
    b9 = Entry(window, font=('arial', 20), width=25)
    b9.grid(row=3, column=2)

    menubar = Menu(window)
    window.config(menu=menubar)
    filemenu = Menu(menubar, tearoff=0)
    settingmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(
        label="Zamknij",
        menu=filemenu)
    menubar.add_cascade(
        label="Narzędzia Administracyje",
        menu=settingmenu)
    filemenu.add_command(label="Wyjście", command=window.quit)
    settingmenu.add_command(label="Panel Administratora", command=pasword2)
    settingmenu.add_command(label="Czyszczenie Bazy Sprawozdań Produkcyjnych", command=pasword)
    var.trace_add('write', to_upper)
    var1.trace_add('write', to_upper)
    var2.trace_add('write', to_upper)


'''
TWORZENIE MATERIAŁÓWKI
TWORZENIE MATERIAŁÓWKI
TWORZENIE MATERIAŁÓWKI
'''

def materialy():
    window = Tk()
    window.title("Tworzenie Materiału")
    window.geometry('850x400')
    window.config(background='#b3b3b3')
    con = sqlite3.connect('factory_db')
    cur = con
    #cur.execute('drop table material')
    cur.execute(
        'create table if not exists material (id integer primary key autoincrement,numer_materialu,numer_klienta,wydajnosc)')

    def uzupelnione():
        if b1.get():
            if b2.get():
                if b3.get():
                    messagebox.showinfo('Informacja Systemowa', 'Wszystkie Dane Uzupełniono Poprawnie')
                    zatwierdz()
                else:
                    messagebox.showinfo('Błąd Danych', 'Wydajność Musi Zostać Określona')
            else:
                messagebox.showerror('Błąd Danych', 'Numer Klienta Musi Zostać Nadany')
        else:
            messagebox.showerror('Błąd Danych', 'Numer Materiału Musi Zostać Uzupełniony')

    def uzupelnione1():
        if b1.get():
            if b2.get():
                if b3.get():
                    messagebox.showinfo('Informacja', 'Wszystkie Dane Uzupełniono Poprawnie')
                    zmien()
                else:
                    messagebox.showinfo('Błąd Danych', 'Wydajność Musi Zostać Określona')
            else:
                messagebox.showerror('Błąd Danych', 'Numer Klienta Musi Zostać Nadany')
        else:
            messagebox.showerror('Błąd Danych', 'Numer Materiału Musi Zostać Uzupełniony')

    def zatwierdz():
        # window = Tk()
        # window.geometry('850x400')
        # window.configure(background='#b3b3b3')
        con = sqlite3.connect('factory_db')
        cur = con
        cur.execute(
            'insert into material (numer_materialu,numer_klienta,wydajnosc) values(:numer_mat,:num_kl,:wydajnosc)', {
                'numer_mat': b1.get(),
                'num_kl': b3.get(),
                'wydajnosc': b2.get()
            })
        con.commit()
        b1.delete(0, END)
        b2.delete(0, END)
        b3.delete(0, END)
        messagebox.showinfo("Informacja Systemowa", "Dodano Nowy Materiał do tabeli")

    def sprawdz():
        con = sqlite3.connect('factory_db')
        cur = con
        results=cur.execute('select * from material')
        d=results.fetchall()
        if len(d)>0:
            window = Tk()
            window.geometry('850x400')
            window.configure(background='#b3b3b3')
            columns = ('c1', 'c2', 'c3', 'c4')
            tree = ttk.Treeview(window, columns=columns, show='headings', height=52)
            tree.heading('c1', text='Id')
            tree.heading('c2', text='Numer Materiału')
            tree.heading('c3', text='Numer Cześci Gotowej')
            tree.heading('c4', text='Określona wydajnosć')
            for row in cur.execute('select id,numer_materialu,numer_klienta,wydajnosc from material'):
                tree.insert('', tk.END, values=(row[0], row[1], row[2], row[3]))
                tree.grid(row=0, column=0, sticky='n')
                # add a scrollbar
                scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
                tree.configure(yscroll=scrollbar.set)
                scrollbar.grid(row=0, column=1, sticky='ns')
                con.commit()
        if len(d)<1:
            messagebox.showinfo('Informacja Systemowa','Baza Materiałów jest Pusta')
    def zmien():
        con = sqlite3.connect('factory_db')
        cur = con
        cur.execute(
            'update material set numer_materialu=:num1,numer_klienta=:num2,wydajnosc=:num3 where numer_materialu=:num4',
            {
                'num1': b1.get(),
                'num2': b3.get(),
                'num3': b2.get(),
                'num4': b1.get()
            })
        con.commit()
        b1.delete(0, END)
        b2.delete(0, END)
        b3.delete(0, END)
        messagebox.showinfo("Informacja Systemowa", "Dane W Tabeli Zostały Zamienione")

    def pasword():
        def f1():
            if bb7.get() == c1:
                q = tk.messagebox.askyesno('Czyszczenie Tabeli', "Chcesz Wyczyścić Bazę Materiałów?")
                if q == 1:
                    cur.execute("delete from material")
                    con.commit()
                    messagebox.showinfo('Informacja Systemowa', 'Baza Została Wyczyszczona')
                    window.destroy()
                    window1.destroy()
                elif q == 0:
                    time.sleep(5)
                    messagebox.showinfo('Informacja Systemowa', 'Działanie Zostało Przerwane')
                    window1.destroy()
                    window.destroy()
            else:
                messagebox.showinfo('Błąd Danych', 'Hasło Nie Jest Poprawne')

        window1 = Tk()
        window1.geometry('450x300')
        window1.title('Weryfikacja Uprawnień')
        window1.configure(background='#b3b3b3')
        ll = Label(window1, text='Podaj Hasło', font=('arial', 25),background='white')
        ll.grid(row=1, column=1, sticky='N', padx=20, pady=20)
        c1 = 'admin1'
        bb7 = Entry(window1, font=('arial', 25),show='*')
        bb7.grid(row=2, column=1, sticky='N', padx=20, pady=20)
        bb2 = Button(window1, text='Wejdź', command=f1)
        bb2.grid(row=3, column=1, sticky='N', padx=20, pady=20)

    def to_upper(*args):
        var.set(var.get().upper())
        var1.set(var1.get().upper())
        var2.set(var2.get().upper())

    var = tk.StringVar(window)
    var1 = tk.StringVar(window)
    var2 = tk.StringVar(window)

    l1 = Label(window, text='Nadaj Numer Materiału:', font=('arail', 20), background='white')
    l1.grid(row=1, column=0, pady=10, padx=10, sticky='W')
    b1 = Entry(window, font=('arail', 20),textvariable=var)
    b1.grid(row=1, column=1, padx=10, pady=8, sticky='W')
    l2 = Label(window, text='Określ Wydajność:', font=('arial', 20), background='white')
    l2.grid(row=3, column=0, pady=10, padx=10, sticky='W')
    b2 = Entry(window, font=('arail', 20),textvariable=var1)
    b2.grid(row=3, column=1, padx=10, pady=8, sticky='W')
    l3 = Label(window, text='Nadaj Numer Częsci Klienta:', font=('arial', 20), background='white')
    l3.grid(row=2, column=0, pady=10, padx=10, sticky='W')
    b3 = Entry(window, font=('arail', 20),textvariable=var2)
    b3.grid(row=2, column=1, padx=10, pady=8, sticky='W')
    b4 = Button(window, text='Zatwierdź', width=15, command=uzupelnione, font=('arial', 20))
    b4.grid(row=5, column=1, padx=10, pady=10, sticky='W')
    b5 = Button(window, text='Sprawdź', command=sprawdz, width=15, font=('arial', 20))
    b5.grid(row=4, column=0, padx=10, pady=10, sticky='W')
    b6 = Button(window, text='Zmień', command=uzupelnione1, width=15, font=('arial', 20))
    b6.grid(row=4, column=1, padx=10, pady=10, sticky='W')
    menubar = Menu(window)
    window.config(menu=menubar)
    filemenu = Menu(menubar, tearoff=0)
    settingmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(
        label="Zamknij",
        menu=filemenu)
    menubar.add_cascade(
        label="Narzędzia Administracyje",
        menu=settingmenu)
    filemenu.add_command(label="Wyjście", command=window.quit)
    settingmenu.add_command(label="Czyszczenie Bazy Materiałów", command=pasword)
    var.trace_add('write', to_upper)
    var1.trace_add('write', to_upper)
    var2.trace_add('write', to_upper)
'''
ZUŻYCIE MATERIAŁÓW
ZUŻYCIE MATERIAŁÓW
ZUŻYCIE MATERIAŁÓW
ZUŻYCIE MATERIAŁÓW
'''

def zuzycie():
    window2 = Tk()
    window2.title("Zużycie Materiału")
    window2.geometry('350x250')
    window2.config(background='#b3b3b3')
    def wybor_daty():
        dt = cal.get_date()
        str_dt4 = dt.strftime("%Y-%m-%d")
        window = Tk()
        window.geometry('750x450')
        window.config(background='#b3b3b3')
        con = sqlite3.connect('factory_db')
        cur = con
        columns = ('c1', 'c2', 'c3')
        tree = ttk.Treeview(window, columns=columns, show='headings', height=52)
        # define headings
        tree.heading('c1', text='Numer Materiału')
        tree.heading('c2', text='Zużycie Materiału')
        tree.heading('c3', text='Data')
        results=cur.execute('select * from status_produkcji')
        w=results.fetchall()
        if len(w)>0:
            for row in cur.execute('select product,sum(qty+qty1),date from status_produkcji where date >= (?) group by product',
                               (str_dt4,)):
                tree.insert('', tk.END, values=(row[0], row[1], row[2]))
                tree.grid(row=0, column=0, sticky='n')
                # add a scrollbar
                scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
                tree.configure(yscroll=scrollbar.set)
                scrollbar.grid(row=0, column=1, sticky='ns')
                con.commit()
        else:
            window.iconify()
            messagebox.showinfo('Informacja Systemowa',"Baza Danych Statusu Produkcji Jest Czysta Nie Można Obliczyć Zużycia")
            window.destroy()
            window2.destroy()

    cal = DateEntry(window2, selectmode='day', date_pattern='yyyy-MM-dd',font=('arial',20))
    cal.grid(row=1, column=0, padx=15, pady=10)
    b2 = Button(window2, text='Przelicz Materiał', command=wybor_daty, font=('arial', 20))
    b2.grid(row=2, column=0, padx=10, pady=10, sticky='W')

'''
Zamówienia
Zamówienia
Zamówienia
'''

def zam():
    window=Tk()
    window.title("Identyfikacja Zamówień")
    window.geometry('850x550')
    window.config(background='#b3b3b3')
    con = sqlite3.connect('factory_db')
    cur = con
    cur.execute(
        'create table if not exists zamowienia(id integer primary key autoincrement,numer_zamowienia,numer_cz_gotowej,ilosc,data_dostawy,status)')

    def zamowienie():
        con = sqlite3.connect('factory_db')
        cur = con
        if b1.get():
                con=sqlite3.connect('factory_db')
                cur=con
                results = cur.execute('select * from material where numer_klienta=?', (b1.get(),))
                w=results.fetchall()
                if len(w)>=0:
                    cur.execute('insert into zamowienia(numer_zamowienia,numer_cz_gotowej,ilosc,data_dostawy,status) values(:numer_zamowienia,:numer_cz_gotowej,:ilosc,:data_dostawy,:status)',
                    {
                    'numer_zamowienia': b4.get(),
                    'numer_cz_gotowej': b1.get(),
                    'ilosc': b2.get(),
                    'data_dostawy': cal.get_date(),
                    'status': b3.get()
                    })
                    con.commit()
                    messagebox.showinfo('Informacja Systemowa','Dodano Nowe Zamówienie')
                    b1.delete(0, END)
                    b2.delete(0, END)
                    b3.delete(0, END)
                    b4.delete(0, END)
                if len(w)<1:
                    messagebox.showinfo('Informacja Systemowa','Podany Numer Częsci Gotwej Nie Istnieje W Systemie')
    def pasword():
        def f1():
            if bb7.get() == c1:
                q = tk.messagebox.askyesno('Informacja Systemowa', "Chcesz Wyczyścić Bazę Zamówień?")
                if q == 1:
                    cur.execute("delete from zamowienia")
                    con.commit()
                    messagebox.showinfo('Informacja Systemowa', 'Baza Zamówień Została Wyczyszczona')
                    window.destroy()
                    window1.destroy()
                elif q == 0:
                    time.sleep(5)
                    messagebox.showinfo('Informacja Systemowa', 'Działanie Zostało Przerwane')
                    window1.destroy()
                    window.destroy()
            else:
                messagebox.showinfo('Błąd Danych', 'Hasło Nie Jest Poprawne')
        window1 = Tk()
        window1.geometry('450x300')
        window1.configure(background='#b3b3b3')
        window1.title('Weryfikacja Uprawnień')
        ll = Label(window1, text='Podaj Hasło', font=('arial', 25),background='white')
        ll.grid(row=1, column=1, sticky='N', padx=20, pady=20)
        c1 = 'admin1'
        bb7 = Entry(window1, font=('arial', 25),show='*')
        bb7.grid(row=2, column=1, sticky='N', padx=20, pady=20)
        bb2 = Button(window1, text='Wejdź', command=f1)
        bb2.grid(row=3, column=1, sticky='N', padx=20, pady=20)

    def sprawdz():
        con=sqlite3.connect('factory_db')
        cur=con
        results=cur.execute('select * from zamowienia')
        w=results.fetchall()
        if len(w)>0:
            window = Tk()
            window.geometry('1250x450')
            window.config(background='#b3b3b3')
            columns = ('c1', 'c2', 'c3', 'c4', 'c5', 'c6')
            tree = tk.ttk.Treeview(window, columns=columns, show='headings', height=52)
            # define headings
            tree.heading('c1', text='Id')
            tree.heading('c2', text='Numer Zamówienia')
            tree.heading('c3', text='Numer Części Gotowej')
            tree.heading('c4', text='Zamówiona Ilość')
            tree.heading('c5', text='Data Dostawy Do Klienta')
            tree.heading('c6', text='Status')
            # add data to the treeview
            con = sqlite3.connect('factory_db')
            cur = con
            for row in cur.execute('select * from zamowienia'):
                tree.insert('', tk.END, values=(row[0], row[1], row[2], row[3], row[4], row[5]))
                tree.grid(row=0, column=0, sticky='NE')
                # add a scrollbar
                scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
                tree.configure(yscroll=scrollbar.set)
                scrollbar.grid(row=0, column=1, sticky='ns')
                con.commit()
        if len(w)<1:
            messagebox.showinfo('Informacja Systemowa','Baza Danych Zamówień Jest Czysta')

    def zmiana_statusu():
        def zmiana():
            con = sqlite3.connect('factory_db')
            cur = con
            results= cur.execute('select* from zamowienia where numer_zamowienia=?',(b11.get(),))
            d=results.fetchall()
            if len(d)>0:
                cur.execute('update zamowienia set status =? where numer_zamowienia=?', (b12.get(), b11.get()))
                con.commit()
                messagebox.showinfo('Informacja Systemowa','Zamówienie Zostało Zmienione')
                b11.delete(0, END)
                b12.delete(0, END)
            if len(d)<1:
                messagebox.showinfo('Błąd Danych','Numer Zamówienie Musi Być Uzupełniony')

        def to_upper(*args):
            var.set(var.get().upper())
            var1.set(var1.get().upper())

        window = Tk()
        window.title('Zmiana Statusu Zamówienia')
        var = tk.StringVar(window)
        var1 = tk.StringVar(window)

        window.geometry('750x300')
        window.config(background='#b3b3b3')
        l11 = Label(window, text='Podaj Numer Zamówienia:',font=('arial', 20),background='white')
        l11.grid(row=1, column=0, pady=10, padx=10,sticky='w')
        b11 = Entry(window, font=('arial', 20),textvariable=var )
        b11.grid(row=1, column=2, padx=10, pady=10)
        l12 = Label(window, text='Podaj Nowy Status:', font=('arial', 20),background='white')
        l12.grid(row=2, column=0, pady=10, padx=10,sticky='w')
        b12 = Entry(window, font=('arial', 20),textvariable=var1 )
        b12.grid(row=2, column=2, padx=10, pady=10)
        b13 = Button(window, text='Akceptuj Zmiany', command=zmiana, font=('arial', 20))
        b13.grid(row=3, column=2, padx=50, pady=10, sticky='N')
        var.trace_add('write', to_upper)
        var1.trace_add('write', to_upper)

    def to_upper(*args):
        var.set(var.get().upper())
        var1.set(var1.get().upper())
        var2.set(var2.get().upper())
        var3.set(var3.get().upper())

    var = tk.StringVar(window)
    var1 = tk.StringVar(window)
    var2 = tk.StringVar(window)
    var3 = tk.StringVar(window)

    menubar = Menu(window)
    window.config(menu=menubar)
    filemenu = Menu(menubar, tearoff=0)
    settingmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(
        label="Zamknij",
        menu=filemenu)
    menubar.add_cascade(
        label="Narzędzia Administracyje",
        menu=settingmenu)
    filemenu.add_command(label="Wyjście", command=window.quit)
    settingmenu.add_command(label="Wyczyść Bazę Danych Zamówień", command=pasword)
    l1 = Label(window, text='Wprowadź Numer Części Gotowej:', font=('arail', 20), background='white')
    l1.grid(row=1, column=0, pady=10, padx=10, sticky='W')
    b1 = Entry(window, font=('arail', 20),textvariable=var)
    b1.grid(row=1, column=1, padx=10, pady=8, sticky='W')
    l2 = Label(window, text='Ustal Wielkosć Zamówienia:', font=('arail', 20), background='white')
    l2.grid(row=2, column=0, pady=10, padx=10, sticky='W')
    b2 = Entry(window, font=('arail', 20),textvariable=var1)
    b2.grid(row=2, column=1, padx=10, pady=8, sticky='W')
    l3 = Label(window, text='Status:', font=('arail', 20), background='white')
    l3.grid(row=3, column=0, pady=10, padx=10, sticky='W')
    b3 = Entry(window, font=('arail', 20),textvariable=var2)
    b3.grid(row=3, column=1, padx=10, pady=8, sticky='W')
    l4 = Label(window, text='Numer Zamówienia:', font=('arail', 20), background='white')
    l4.grid(row=4, column=0, pady=10, padx=10, sticky='W')
    b4 = Entry(window, font=('arail', 20),textvariable=var3)
    b4.grid(row=4, column=1, padx=10, pady=8, sticky='W')
    b5 = Button(window, text='Wprowadź', command=zamowienie, width=20, font=('arial', 20))
    b5.grid(row=6, column=1, padx=10, pady=20, sticky='W')
    b6 = Button(window, text='Sprawdź zamówienia', command=sprawdz, width=20, font=('arial', 20))
    b6.grid(row=7, column=0, padx=10, pady=20, sticky='W')
    b7 = Button(window, text='Zmień Status', command=zmiana_statusu, width=20, font=('arial', 20))
    b7.grid(row=7, column=1, padx=10, pady=20, sticky='W')
    cal_lab=Label(window, text='Podaj Datę Dostawy:', font=('arail', 20), background='white')
    cal_lab.grid(row=5, column=0, padx=10,pady=20, sticky='W')
    cal = DateEntry(window, selectmode='day', date_pattern='yyyy-MM-dd',font=('arial',20))
    cal.grid(row=5, column=1, padx=15,sticky='W')
    var.trace_add('write', to_upper)
    var1.trace_add('write', to_upper)
    var2.trace_add('write', to_upper)
    var3.trace_add('write', to_upper)


def okienko():
    #tworznie widoku z 5 przyciskami
    window = Tk()
    window.title('System Zarządzania Przedsiębiorstwem')
    window.geometry('450x400')
    window.config(background='#b3b3b3')
    b1=Button(window, text='Ewidencja Czasu Pracy',command=czas_pracy,font=('arial',15),width=20)
    b1.grid(row=1,column=0,padx=10,pady=10,sticky='W')

    b2=Button(window, text='Karta Pracownika',command=karta_pers,font=('arial',15),width=20)
    b2.grid(row=2,column=0,padx=10,pady=10,sticky='W')

    b3=Button(window, text='Status Produkcji',command=produkcja,font=('arial',15),width=20)
    b3.grid(row=3,column=0,padx=10,pady=10,sticky='W')

    b4=Button(window, text='Karta Materiałowa',command=materialy,font=('arial',15),width=20)
    b4.grid(row=4,column=0,padx=10,pady=10,sticky='W')

    b5=Button(window, text='Zużycie Materiałów',command=zuzycie,font=('arial',15),width=20)
    b5.grid(row=5,column=0,padx=10,pady=10,sticky='W')

    b6=Button(window, text='Zamówienia',command=zam,font=('arial',15),width=20)
    b6.grid(row=6,column=0,padx=10,pady=10,sticky='W')
    window.mainloop()

okienko()
