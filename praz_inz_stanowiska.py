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

'''
 MODUŁ KADR - NUMERY PERSONALNE ORAZ PRAWOCOWNICY

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
    #cur.execute('drop table pracownicy')
    cur.execute(
        'create table if not exists numery_personalne (id integer primary key autoincrement,numer_personalny,nazwa_dzialu)')

    #cur.execute('drop table numery_personalne')
    def save():
        if b1.get() and b2.get() and b3.get() and b4.get() and b5.get():
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
                'insert into numery_personalne (numer_personalny,nazwa_dzialu)values(:numer_personalny,:nazwa_dzialu)',
                {
                    'numer_personalny': b4.get(),
                    'nazwa_dzialu': b5.get()
                })
            con.commit()
            tk.messagebox.showinfo('Informacja', 'Wpis Został Utworzony')
            b1.delete(0, END)
            b2.delete(0, END)
            b3.delete(0, END)
            b4.delete(0, END)
            b5.delete(0, END)

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
                    'update numery_personalne set numer_personalny = :numer_personalny,nazwa_dzialu = :nazwa_dzialu, where numer_personalny = :numer_personalny',
                    {
                        'numer_personalny': b4.get(),
                        'nazwa_dzialu': b5.get(),
                    })
                con.commit()
                tk.messagebox.showinfo('Informacja', 'Zmainy Zostały Zapisane')
                b1.delete(0, END)
                b2.delete(0, END)
                b3.delete(0, END)
                b4.delete(0, END)
                b5.delete(0, END)

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
                            tk.messagebox.showinfo('OK', 'Wszystkie Parametry Zostały Przypisane Poprawnie')
                            checking()

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
        con = sqlite3.connect('factory_db')
        cur = con
        results=cur.execute('select * from pracownicy')
        w=results.fetchall()
        if len(w)>0:
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
        else:
            messagebox.showinfo('Informacja Systemowa','Baza Danych Jest Pusta')


    def display_numery_pers():
        con = sqlite3.connect('factory_db')
        cur = con
        results=cur.execute('select * from numery_personalne')
        w=results.fetchall()
        if len(w)>0:
            window = tk.Tk()
            window.title('Numery Personalne')
            window.geometry('650x800')
            window.configure(background='#b3b3b3')
            # define columns
            columns = ('c1', 'c2', 'c3')
            tree = tk.ttk.Treeview(window, columns=columns, show='headings', height=52)
            # define headings
            tree.heading('c1', text='Id')
            tree.heading('c2', text='Numer Personalny')
            tree.heading('c3', text='Nazwa Działu')

            # add data to the treeview
            con = sqlite3.connect('factory_db')
            cur = con
            for row in cur.execute(
                'select id,numer_personalny,nazwa_dzialu from numery_personalne'):
                tree.insert('', tk.END, values=(row[0], row[1], row[2]))
                tree.grid(row=0, column=0, sticky='NE')
                # add a scrollbar
                scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
                tree.configure(yscroll=scrollbar.set)
                scrollbar.grid(row=0, column=1, sticky='ns')
                con.commit()
        else:
            messagebox.showinfo('Informacja Systemowa','Baza Danych Jest Pusta')

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
        messagebox.showinfo('Informacja Systemowa','Baza Danych Została Zaimportowana')
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
                    time.sleep(1)
                    messagebox.showinfo('Informacja Systemowa', 'Działanie Zostało Przerwane, Baza Danych Nie Została Wyczyszczona')
                    window1.destroy()
                    window.destroy()
            else:
                messagebox.showinfo('Błąd Danych', 'Hasło Nie Jest Poprawne')

        window1 = Tk()
        window1.geometry('450x300')
        window1.title('Weryfikacja Uprawnień')
        window1.configure(background='#b3b3b3')
        ll = Label(window1, text='Podaj Hasło', font=('arial', 25), background='white')
        ll.grid(row=1, column=1, sticky='N', padx=20, pady=20)
        c1 = 'admin1'
        bb7 = Entry(window1, font=('arial', 25), show='*')
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
                    time.sleep(1)
                    window.destroy()
                    window1.destroy()
                    messagebox.showinfo('Informacja Systemowa', 'Działanie Zostało Przerwane, Baza Danych Nie Została Wyczyszczona')
            else:
                messagebox.showinfo('Błąd Danych', 'Hasło Nie Jest Poprawne')

        window1 = Tk()
        window1.geometry('450x300')
        window1.title('Weryfikacja Uprawnień')
        window1.configure(background='#b3b3b3')
        ll = Label(window1, text='Podaj Hasło', font=('arial', 25), background='white')
        ll.grid(row=1, column=1, sticky='N', padx=20, pady=20)
        c1 = 'admin1'
        bb7 = Entry(window1, font=('arial', 25), show='*')
        bb7.grid(row=2, column=1, sticky='N', padx=20, pady=20)
        bb2 = Button(window1, text='Wejdź', command=f1)
        bb2.grid(row=3, column=1, sticky='N', padx=20, pady=20)


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
    l4 = Label(window, text='Nadaj Numer Personalny Pracownika:', font=('arial', 20), background='white')
    l4.grid(row=4, column=0, pady=10, padx=10, sticky='W')
    b4 = Entry(window, textvariable=var3, font=('arail', 25))
    b4.grid(row=4, column=2, padx=10, pady=8, sticky='N')
    l5 = Label(window, text='Podaj Nazwę Struktury Organizacyjnej:', font=('arial', 20), background='white')
    l5.grid(row=5, column=0, pady=10, padx=10, sticky='W')
    b5 = Entry(window, textvariable=var4, font=('arail', 25))
    b5.grid(row=5, column=2, padx=10, pady=8, sticky='N')
    b8 = Button(window, text='SPRAWDŹ', command=veryfication, font=('arial', 30), background='#3399ff')
    b8.grid(row=8, column=0, padx=10, pady=50, sticky='N')
    b9 = Button(window, text='ZATWIERDŹ', command=save, font=('arial', 30), background='Green')
    b9.grid(row=8, column=2, padx=10, pady=50, sticky='N')

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
    settingmenu.add_command(label="Podglą Tabeli Pracowników", command=display_pracownicy)
    settingmenu.add_command(label="Podglą Tabeli Numerów Personalnych",command=display_numery_pers )
    settingmenu.add_command(label="Czyszczenie Tabeli Pracowników", command=pasword)
    settingmenu.add_command(label="Czyszczenie Tabeli Numery Personalne", command=pasword2)
    settingmenu.add_separator()
    settingmenu.add_cascade(label='Pobierz Listę Pracowników', command=to_excel)



def karta_maszyn():
    window = Tk()
    window.title('Karta Maszyn')
    window.config(background='#b3b3b3')
    window.state('zoomed')

    # creating Databases
    con = sqlite3.connect('factory_db')
    cur = con
    cur.execute(
       'create table if not exists maszyny (id integer primary key autoincrement, marka, model,typ,rok_produkcji)')
    #cur.execute('drop table maszyny')
    
    def save_m():
        if b1.get() and b2.get() and b3.get() and b4.get():
            con = sqlite3.connect('factory_db')
            cur = con
            cur.execute(
                'insert into maszyny (marka,model,typ,rok_produkcji) values(:marka,:model,:typ,:rok_produkcji)',
                {
                    'marka': b1.get(),
                    'model': b2.get(),
                    'typ': b3.get(),
                    'rok_produkcji': b4.get()
                })
            con.commit()
            tk.messagebox.showinfo('Informacja', 'Wpis Został Utworzony')
            b1.delete(0, END)
            b2.delete(0, END)
            b3.delete(0, END)
            b4.delete(0, END)
        else:
            tk.messagebox.showwarning('Błąd Danych', 'Brakuje Jednego Z Wymaganych Pól')

    def change_m():
        con = sqlite3.connect('factory_db')
        cur = con
        cur.execute(
            'update maszyny set marka = :marka,model = :model,typ = :typ,rok_produkcji = :rok_produkcji where id = :id',
        {
            'marka': b1.get(),
            'model': b2.get(),
            'typ': b3.get(),
            'rok_produckji': b4.get(),
            'id':b5.get()
        })
        con.commit()
        tk.messagebox.showinfo('Informacja', 'Zmainy Zostały Zapisane')
        b1.delete(0, END)
        b2.delete(0, END)
        b3.delete(0, END)
        b4.delete(0, END)
        b5.delete(0, END)

    def veryfication_m():
        if b1.get():
            if b2.get():
                if b3.get():
                    if b4.get():
                        if b5.get():
                            tk.messagebox.showinfo('OK', 'Wszystkie Parametry Zostały Przypisane Poprawnie')
                            change_m()
                        else:
                            tk.messagebox.showerror('Error', 'Numer ID Musi Zostać Uzupełniony')
                    else:
                        tk.messagebox.showerror('Error', 'Rok Maszyny Musi Zostać Podany')
                else:
                    tk.messagebox.showerror('Error', 'Typ Maszyny Musi Zostać Podany')
            else:
                tk.messagebox.showerror('Error', 'Model Maszyny Musi ZOstać Podany')
        else:
            tk.messagebox.showerror('Error', 'Marka Maszyny Musi Zostać Podana')

    def display_maszyny():
        con = sqlite3.connect('factory_db')
        cur = con
        results=cur.execute('select * from maszyny')
        w=results.fetchall()
        if len(w)>0:
            window = tk.Tk()
            window.title('Spis Maszyn')
            window.geometry('1050x800')
            window.configure(background='#b3b3b3')
            # define columns
            columns = ('c1', 'c2', 'c3', 'c4', 'c5')
            tree = tk.ttk.Treeview(window, columns=columns, show='headings', height=52)
            # define headings
            tree.heading('c1', text='Id')
            tree.heading('c2', text='Marka Maszyny')
            tree.heading('c3', text='Model Maszyny')
            tree.heading('c4', text='Typ Maszyny')
            tree.heading('c5', text='Rok Produckju')

            # add data to the treeview
            con = sqlite3.connect('factory_db')
            cur = con
            for row in cur.execute('select id,marka, model, typ,rok_produkcji from maszyny'):
                tree.insert('', tk.END, values=(row[0], row[1], row[2], row[3], row[4]))
                tree.grid(row=0, column=0, sticky='n')
                # add a scrollbar
                scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
                tree.configure(yscroll=scrollbar.set)
                scrollbar.grid(row=0, column=1, sticky='ns')
                con.commit()
        else:
            messagebox.showinfo('Informacja Systemowa','Baza Danych Jest Pusta')


    def to_excel():
        workbook = Workbook('Zestawienie_Maszyn.xlsx')
        worksheet = workbook.add_worksheet('Charakterystyka Maszyn')
        con = sqlite3.connect('factory_db')
        cur = con
        mysel = cur.execute("select * from maszyny")
        for i, row in enumerate(mysel):
            for j, value in enumerate(row):
                worksheet.write(i, j, row[j])
        messagebox.showinfo('Informacja Systemowa','Baza Danych Została Zaimportowana')
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
                q = tk.messagebox.askyesno('Informacja Systemowa', "Chcesz Wyczyścić Bazę Maszyn?")
                if q == 1:
                    cur.execute("delete from maszyny")
                    con.commit()
                    messagebox.showinfo('Informacja Systemowa', 'Baza Maszyn Została Wyczyszczona')
                    window1.title('Weryfikacja Uprawnień')
                    window.destroy()
                elif q == 0:
                    time.sleep(1)
                    messagebox.showinfo('Informacja Systemowa', 'Działanie Zostało Przerwane, Baza Danych Nie Została Wyczyszczona')
                    window1.destroy()
                    window.destroy()
            else:
                messagebox.showinfo('Błąd Danych', 'Hasło Nie Jest Poprawne')

        window1 = Tk()
        window1.geometry('450x300')
        window1.title('Weryfikacja Uprawnień')
        window1.configure(background='#b3b3b3')
        ll = Label(window1, text='Podaj Hasło', font=('arial', 25), background='white')
        ll.grid(row=1, column=1, sticky='N', padx=20, pady=20)
        c1 = 'admin1'
        bb7 = Entry(window1, font=('arial', 25), show='*')
        bb7.grid(row=2, column=1, sticky='N', padx=20, pady=20)
        bb2 = Button(window1, text='Wejdź', command=f1)
        bb2.grid(row=3, column=1, sticky='N', padx=20, pady=20)

    var = tk.StringVar(window)
    var1 = tk.StringVar(window)
    var2 = tk.StringVar(window)
    var3 = tk.StringVar(window)
    var4 = tk.StringVar(window)
    var5 = tk.StringVar(window)
    var6 = tk.StringVar(window)

    l_tit = Label(window, text='Zakładanie Karty Maszyn', font=('arial', 40), background='white')
    l_tit.grid(row=0, column=0, pady=20, columnspan=1, sticky='N')
    l1 = Label(window, text='Podaj Markę:', font=('arail', 20), background='white')
    l1.grid(row=1, column=0, pady=10, padx=10, sticky='W')
    b1 = Entry(window, textvariable=var, font=('arail', 25))
    b1.grid(row=1, column=2, padx=10, pady=8, sticky='W')
    l2 = Label(window, text='Podaj Model:', font=('arial', 20), background='white')
    l2.grid(row=2, column=0, pady=10, padx=10, sticky='W')
    b2 = Entry(window, textvariable=var1, font=('arail', 25))
    b2.grid(row=2, column=2, padx=10, pady=8, sticky='N')
    l3 = Label(window, text='Podaj Typ:', font=('arial', 20), background='white')
    l3.grid(row=3, column=0, pady=10, padx=10, sticky='W')
    b3 = Entry(window, textvariable=var2, font=('arail', 25))
    b3.grid(row=3, column=2, padx=10, pady=8, sticky='N')
    l4 = Label(window, text='Podaj Rok Produkcji:', font=('arial', 20), background='white')
    l4.grid(row=4, column=0, pady=10, padx=10, sticky='W')
    b4 = Entry(window, textvariable=var3, font=('arail', 25))
    b4.grid(row=4, column=2, padx=10, pady=8, sticky='N')
    l5 = Label(window, text='Podaj ID:', font=('arial', 20), background='white')
    l5.grid(row=5, column=0, pady=10, padx=10, sticky='W')
    b5 = Entry(window, textvariable=var4, font=('arail', 25))
    b5.grid(row=5, column=2, padx=10, pady=8, sticky='N')
    b8 = Button(window, text='SPRAWDŹ', command=veryfication_m, font=('arial', 30), background='#3399ff')
    b8.grid(row=8, column=0, padx=10, pady=50, sticky='N')
    b9 = Button(window, text='ZATWIERDŹ', command=save_m, font=('arial', 30), background='Green')
    b9.grid(row=8, column=2, padx=10, pady=50, sticky='N')

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
    settingmenu.add_command(label="Podglą Tabeli Maszyn", command=display_maszyny)
    settingmenu.add_command(label="Czyszczenie Tabeli Maszyn", command=pasword)
    settingmenu.add_separator()
    settingmenu.add_cascade(label='Pobierz Listę Maszyn', command=to_excel)


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



    def to_excel_mat():
        workbook = Workbook('materialy.xlsx')
        worksheet = workbook.add_worksheet()
        con = sqlite3.connect('factory_db')
        c = con.cursor()
        con.execute("select * from material")
        mysel = c.execute("select * from material")
        for i, row in enumerate(mysel):
            for j, value in enumerate(row):
                worksheet.write(i, j, row[j])
        messagebox.showinfo('Informacja Systemowa','Baza Danych Została Zaimportowana')
        workbook.close()
        window.destroy()

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
    b4 = Button(window, text='Zatwierdź', width=15, command=uzupelnione, font=('arial', 20),background='green')
    b4.grid(row=5, column=1, padx=10, pady=10, sticky='W')
    b6 = Button(window, text='Zmień', command=uzupelnione1, width=15, font=('arial', 20),background='yellow')
    b6.grid(row=5, column=0, padx=10, pady=10, sticky='W')
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
    settingmenu.add_cascade(label="Sprawdź Bazę Materiałów",command=sprawdz)
    settingmenu.add_separator()
    settingmenu.add_cascade(label="Pobierz Listę Materiałów", command= to_excel_mat)
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

    def to_excel_zam():
        workbook = Workbook('zamowienia.xlsx')
        worksheet = workbook.add_worksheet()
        con = sqlite3.connect('factory_db')
        c = con.cursor()
        con.execute("select * from zamowienia")
        mysel = c.execute("select * from zamowienia")
        for i, row in enumerate(mysel):
            for j, value in enumerate(row):
                worksheet.write(i, j, row[j])
        messagebox.showinfo('Informacja Systemowa','Baza Danych Została Zaimportowana')
        workbook.close()
        window.destroy()


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
                window3.destroy()
            if len(d)<1:
                messagebox.showinfo('Błąd Danych','Numer Zamówienie Musi Być Uzupełniony')

        def to_upper(*args):
            var.set(var.get().upper())
            var1.set(var1.get().upper())


        window3 = Tk()
        window3.title('Zmiana Statusu Zamówienia')
        var = tk.StringVar(window3)
        var1 = tk.StringVar(window3)
        window3.geometry('750x300')
        window3.config(background='#b3b3b3')
        l11 = Label(window3, text='Podaj Numer Zamówienia:',font=('arial', 20),background='white')
        l11.grid(row=1, column=0, pady=10, padx=10,sticky='w')
        b11 = Entry(window3, font=('arial', 20),textvariable=var )
        b11.grid(row=1, column=2, padx=10, pady=10)
        l12 = Label(window3, text='Podaj Nowy Status:', font=('arial', 20),background='white')
        l12.grid(row=2, column=0, pady=10, padx=10,sticky='w')
        b12 = Entry(window3, font=('arial', 20),textvariable=var1 )
        b12.grid(row=2, column=2, padx=10, pady=10)
        b13 = Button(window3, text='Akceptuj Zmiany', command=zmiana, font=('arial', 20))
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
    settingmenu.add_command(label="Sprawdź Bazy Danych Zamówień", command=sprawdz)
    settingmenu.add_command(label="Wyczyść Bazę Danych Zamówień", command=pasword)
    settingmenu.add_separator()
    settingmenu.add_command(label="Pobierz Bazę Zamówień", command=to_excel_zam)


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
    #b6 = Button(window, text='Sprawdź zamówienia', command=sprawdz, width=20, font=('arial', 20))
    #b6.grid(row=7, column=0, padx=10, pady=20, sticky='W')
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



def okienko1():
    #tworznie widoku z 5 przyciskami
    window1 = Tk()
    window1.title('System Zarządzania Przedsiębiorstwem')
    window1.geometry('430x300')
    window1.config(background='#b3b3b3')
    # *****************
    # ***************
    def export_to_excel():
        workbook = Workbook('produkcja.xlsx')
        worksheet = workbook.add_worksheet()
        con = sqlite3.connect('factory_db')
        c = con.cursor()
        con.execute("select * from status_produkcji")
        mysel = c.execute("select * from status_produkcji")
        for i, row in enumerate(mysel):
            for j, value in enumerate(row):
                worksheet.write(i, j, row[j])
        workbook.close()
        messagebox.showinfo('Informacja Systemowa',' Baza Danych Została Zaimportowana')

    def pasword():
        def f1():
            if bb7.get() == c1:
                q = tk.messagebox.askyesno('Informacja Systemowa', "Chcesz Wyczyścić Bazę Status Produckji?")
                if q == 1:
                    cur.execute("delete from status_produkcji")
                    con.commit()
                    messagebox.showinfo('Informacja Systemowa', 'Baza Została Wyczyszczona')
                    window61.destroy()

                elif q == 0:
                    time.sleep(5)
                    messagebox.showinfo('Informacja Systemowa', 'Działanie Zostało Przerwane')
                    window61.destroy()
            else:
                messagebox.showinfo('Błąd Danych', 'Hasło Nie Jest Poprawne')
        window61 = Tk()
        window61.geometry('450x300')
        window61.title('Weryfikacja Uprawnień')
        window61.configure(background='#b3b3b3')
        ll = Label(window61, text='Podaj Hasło', font=('arial', 25),background='white')
        ll.grid(row=1, column=1, sticky='N', padx=20, pady=20)
        c1 = 'admin1'
        bb7 = Entry(window61, font=('arial', 25),show='*')
        bb7.grid(row=2, column=1, sticky='N', padx=20, pady=20)
        bb2 = Button(window61, text='Wejdź', command=f1)
        bb2.grid(row=3, column=1, sticky='N', padx=20, pady=20)
        text = Text(window61, height=20, width=40)  

        #***********************
    def pasword2():
        def f1():
            if bb7.get() == c1:
                window1.destroy()
                window=Tk()
                window.geometry('1450x800')
                # define columns
                columns = ('c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7')
                tree = ttk.Treeview(window, columns=columns, show='headings', height=52)
                # define headings
                tree.heading('c1', text='ID')
                tree.heading('c2', text='Data')
                tree.heading('c3', text='Przedział Czasowy')
                tree.heading('c4', text='Numer Części')
                tree.heading('c5', text='Ilość')
                tree.heading('c6', text='Ilość Częsci Uszkodzonych/NIOK')
                tree.heading('c7', text='Numer Personalny')
                # add data to the treeview
                con = sqlite3.connect('factory_db')
                cur = con
                results=cur.execute('select * from status_produkcji')
                w=results.fetchall()
                if len(w)>0:
                    for row in cur.execute('select id,data,przedział,produkt,qty,qty1,pracownik from status_produkcji'):
                        tree.insert('', tk.END, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                        tree.grid(row=0, column=0, sticky='nsew')
                        # add a scrollbar
                        scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
                        tree.configure(yscroll=scrollbar.set)
                        scrollbar.grid(row=0, column=1, sticky='ns')
                        con.commit()
                else:
                    messagebox.showinfo('Informacaj Systemowa','Baza Danych Jest Czysta')
                    window6.quit()
                    window1.quit()
            else:
                messagebox.showinfo('Błąd Danych', 'Hasło Nie Jest Poprawne')
        window6 = Tk()
        window6.geometry('450x300')
        window6.title('Weryfikacja Uprawnień')
        window6.configure(background='#b3b3b3')
        ll = Label(window6, text='Podaj Hasło', font=('arial', 25),background='white')
        ll.grid(row=1, column=1, sticky='N', padx=20, pady=20)
        c1 = 'admin1'
        bb7 = Entry(window6, font=('arial', 25),show='*')
        bb7.grid(row=2, column=1, sticky='N', padx=20, pady=20)
        bb2 = Button(window6, text='Wejdź', command=f1)
        bb2.grid(row=3, column=1, sticky='N', padx=20, pady=20)
        text = Text(window6, height=20, width=40)    


        #**********************

    def okienko55():
        window55=Tk()
        window55.title('System Ewidencji Produkcji')
        window55.geometry('450x130')
        window55.configure(background='#b3b3b3')
        bb2 = Label(window55, text='Okno Weryfikacji Produkcji',font=('arial', 25),width=20)
        bb2.grid(row=2,sticky='N', padx=20, pady=20)
        menubar = Menu(window55)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_cascade(label="Wyjście", command=window55.quit)
        filemenu.add_cascade(label="Sprawdź Status Produkcji", command=pasword2)
        filemenu.add_cascade(label="Czyszczenie Bazy Sprawozdań Produkcyjnych", command=pasword)
        filemenu.add_separator()
        filemenu.add_cascade(label="Pobierz Status Produkcji", command=export_to_excel)
        menubar.add_cascade(label='Narzędzia Administracyjne',menu=filemenu)
        window55.config(menu=menubar)
        window55.mainloop()


    def statystyka():
        workbook = Workbook('statystyka_danych.xlsx')
        worksheet = workbook.add_worksheet()
        con = sqlite3.connect('factory_db')
        c = con.cursor()
        con.execute("select * from numery_personalne")
        mysel = c.execute("select * from numery_personalne")
        for i, row in enumerate(mysel):
            for j, value in enumerate(row):
                worksheet.write(i, j, row[j])
        worksheet1 = workbook.add_worksheet()
        con.execute("select * from pracownicy")
        mysel = c.execute("select * from pracownicy")
        for i, row in enumerate(mysel):
            for j, value in enumerate(row):
                worksheet1.write(i, j, row[j])
        worksheet2 = workbook.add_worksheet()
        con.execute("select * from status_produkcji")
        mysel = c.execute("select * from status_produkcji")
        for i, row in enumerate(mysel):
            for j, value in enumerate(row):
                worksheet2.write(i, j, row[j])
        worksheet3 = workbook.add_worksheet()
        con.execute("select * from maszyny")
        mysel = c.execute("select * from maszyny")
        for i, row in enumerate(mysel):
            for j, value in enumerate(row):
                worksheet3.write(i, j, row[j])
        workbook.close()





    # ***********
    b10=Button(window1,text='Panel Raportowania',command=okienko,font=('arial',30),background='green')
    b10.grid(row=1,column=1,padx=20,pady=20)
    menubar=Menu(window1)
    filemenu=Menu(menubar,tearoff=0)
    filemenu1=Menu(menubar,tearoff=0)
    filemenu.add_cascade(label='Karta Pracownika',command=karta_pers)
    filemenu.add_cascade(label='Karta Materiałowa', command=materialy)
    filemenu.add_cascade(label='Karta Maszyn',command=karta_maszyn)
    filemenu.add_cascade(label='Zużycie Materiałów', command=zuzycie)
    filemenu.add_cascade(label='Status Produkcji',command=okienko55)
    filemenu.add_cascade(label='Zamówienia', command=zam)
    filemenu1.add_cascade(label='Importuj Dane',command=statystyka)
    menubar.add_cascade(label='Moduły',menu=filemenu)
    menubar.add_cascade(label='Analityka',menu=filemenu1)
    window1.config(menu=menubar)
    window1.mainloop()

def okienko():
    #tworznie widoku z 5 przyciskami
    window = Tk()
    window.title('System Zarządzania Przedsiębiorstwem')
    window.geometry('450x350')
    window.config(background='#b3b3b3')
    window.state('zoomed')

    con = sqlite3.connect('factory_db')
    cur = con
    #cur.execute('drop table status_produkcji')
    #cur.commit()
    cur.execute(
        "create table  if not exists status_produkcji('id' integer primary key autoincrement,produkt not null, qty,qty1,data,pracownik, przedział)")

    dkx = datetime.today()
    dkx1 = dkx.strftime('%Y-%m-%d,%H :%M :%S')
    dkx2 = dkx.strftime('%Y-%m-%d')

    def confirmation():
        con = sqlite3.connect('factory_db')
        cur = con
        cur.execute(
            "insert into status_produkcji(produkt,przedział,qty,qty1,data,pracownik) values(:produkt,:przedział,:qty,:qty1,:data,:pracownik)",
            {
                'produkt': b1.get(),
                'przedział': b8.get(),
                'qty': b2.get(),
                'qty1':b9.get(),
                'data': dkx2,
                'pracownik': b3.get()
            })
        con.commit()
        messagebox.showinfo('Informacja Systemowa','Dane Zostały Zapisane W Bazie')
        b1.delete(0, END)
        b2.delete(0, END)
        b3.delete(0, END)
        b8.delete(0, END)
        b9.delete(0, END)

    def reject():
        b1.delete(0, END)
        b2.delete(0, END)
        b3.delete(0, END)
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
                                        tk.messagebox.showerror("Błąd danych","Przedział Czasowy Poza Zakresem (1-3)")
                                else: tk.messagebox.showerror("Błąd danych", "Nie Podano Numeru Zmiany Lub Podano Niepoprawną Wartość")
                            else:messagebox.showerror("Błąd Danych","Taki Numer Personalny Nie Istnieje W Systemie")
                        else:tk.messagebox.showerror("Błąd danych","Nie Podano Numeru Personalnego")
                else:tk.messagebox.showerror("Błąd Danych","Podany Materiał Nie Istnieje W Systemie")
        else:messagebox.showerror('Błąd Danych',"Podaj Numer Materiału ")

    def show_my():
        if b3.get():
            show_my_results()
            b3.delete(0,END)
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
                'select id,data,przedział,produkt,qty,qty1,pracownik from status_produkcji where pracownik = :pracownik',
                {
                    'pracownik': b3.get()})
            d = w.fetchall()
            if len(d) > 0:
                window = tk.Tk()
                window.title('Moje Rezultaty')
                window.geometry('1450x800')
                window.configure(background='#b3b3b3')
                # define columns
                columns = ('c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7')
                tree = ttk.Treeview(window, columns=columns, show='headings', height=52)
                # define headings
                tree.heading('c1', text='ID')
                tree.heading('c2', text='Data')
                tree.heading('c3', text='Przedział Czasowy')
                tree.heading('c4', text='Numer Części')
                tree.heading('c5', text='Ilość Części OK')
                tree.heading('c6', text='Ilość Częsci NIOK')
                tree.heading('c7', text='Numer Personalny')
                #add data to the treeview
                for row in cur.execute(
                    'select id,data,przedział,produkt,qty,qty1,pracownik from status_produkcji where pracownik = :pracownik',
                    {
                        'pracownik': b3.get()
                    }):
                    tree.insert('', tk.END, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
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

    var = tk.StringVar(window)
    var1 = tk.StringVar(window)
    var2 = tk.StringVar(window)
    var3 = tk.StringVar(window)
    
    l1 = Label(window, text='Podaj Produkowany Artykuł:', font=("arial", 20), background='white')
    l1.grid(padx=20, pady=20, row=1, column=1,sticky='W')
    b1 = Entry(window, width=25, font=('arial', 20))
    b1.grid(padx=20, pady=20, column=2, row=1,sticky='W')
    # Produced qty
    l2 = Label(window, text='Podaj Ilości Zgodne Z Charakterystyką:', font=("arial", 20), background='white')
    l2.grid(padx=20, pady=20, row=2, column=1,sticky='W')
    b2 = Entry(window, width=25, font=('arial', 20))
    b2.grid(padx=20, pady=20, column=2, row=2)
    # Worker details
    l3 = Label(window, text='Podaj Numer Personalny:', font=("arial", 20), background='white')
    l3.grid(padx=20, pady=20, row=4, column=1,sticky='W')
    b3 = Entry(window, width=25, font=('arial', 20),textvariable=var2)
    b3.grid(padx=20, pady=20, row=4, column=2)
    b5 = Button(window, text="Zatwierdź I Dodaj", command=check_if_empty, font=("arial", 20), background="green")
    b5.grid(row=7, column=2)
    b6 = Button(window, text="Odrzuć", command=reject, font=("arial", 20), background="orange")
    b6.grid(row=8, column=2, pady=25)
    b7 = Button(window, text="Pokaż Swoje Rezultaty", command=show_my, font=("arial", 20), background="blue")
    b7.grid(row=7, column=1)
    var=IntVar()
    w= tk.StringVar()
    b8 = ttk.Combobox(window, width = 27, textvariable = w,font=('Arial',20))
    b8['values'] = (' 06:01-10:00', 
                          ' 10:01-14:00',
                          ' 14:01-18:00',
                          ' 18:01-22:00',
                          ' 22:01-02:00',
                          ' 02:01-06:00',
                            ) 
    b8.grid(row=6, column=2)
    l8 = Label(window, text="Podaj Przedział Czasowy:", font=('arial', 20), bg='white')
    l8.grid(row=6, column=1,padx=20,pady=20,sticky='W')
    l9 = Label(window, text="Podaj Ilość Części Uszkodzonych:", font=('arial', 20), bg='white')
    l9.grid(row=3, column=1,padx=20,pady=20,sticky='W')
    b9 = Entry(window, font=('arial', 20), width=25,textvariable=var3)
    b9.grid(row=3, column=2)
    b10=Button(window,text='Zakończ Działanie',command=window.quit,font=('arial',20),background='red')
    b10.grid(row=10,column=2,padx=20,pady=20)
    def to_upper(*args):
        var1.set(var1.get().upper())
        var2.set(var2.get().upper())
        var3.set(var3.get().upper())
    var.trace_add('write', to_upper)
    var1.trace_add('write', to_upper)
    var2.trace_add('write', to_upper)
    var3.trace_add('write', to_upper)
    


okienko1()
