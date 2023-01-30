import pytube
from pytube import YouTube
import random
import tkinter
from tkinter import *
from tkinter import messagebox

def Downloader():
    def Download_only_song():
        def download():
            if B1.get():
                if B2.get():
                    yt = pytube.YouTube(B1.get())
                    yt.streams.filter(only_audio=True).first().download(B2.get())
                    messagebox.showinfo("INFO", "File Was Donwloaded!!!")
                else:
                    yt = pytube.YouTube(B1.get())
                    yt.streams.filter(only_audio=True).first().download('C:\\Users\\48667\\Desktop')
                    messagebox.showinfo("INFO", "File Was Donwloaded And Saved On The Screen!!!")
            else:
                w=B1.get()
                if len(w)>0:
                    messagebox.showerror("Incorrect tracking","Your Tracking Is Incorrect, Please Check")
                else:
                    messagebox.showinfo("Warning","Link Of Audio Has To Be Entried!!!")
        window.geometry('1000x400')
        B1=Entry(window,width=30,font=('Arial',15))
        B1.grid(row=3,column=1,padx=20,pady=20,sticky="W")
        B2=Entry(window,width=30,font=('Arial',15))
        B2.grid(row=4,column=1,padx=20,pady=20,sticky="W")
        L1=Label(window,text="Please Entry Your Link: ",width=25,font=('Arial',15))
        L1.grid(row=3,column=0,sticky="W")
        L2=Label(window,text="Please Choose Place In PC: ",width=25,font=('Arial',15))
        L2.grid(row=4,column=0,sticky="W")
        B3=Button(window,text="Download",command=download,font=("arial",25),background='green')
        B3.grid(row=5,column=0)

    def Download_full():
        def download():
            if B1.get():
                if B2.get():
                    yt = pytube.YouTube(B1.get())
                    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(B2.get())
                    messagebox.showinfo("INFO", "File Was Donwloaded!!!")
                else:
                    yt = pytube.YouTube(B1.get())
                    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('C:\\Users\\48667\\Desktop')
                    messagebox.showinfo("INFO", "File Was Donwloaded And Saved On The Screen!!!")
            else:
                w = B1.get()
                if len(w) > 0:
                    messagebox.showerror("Incorrect tracking", "Your Tracking Is Incorrect, Please Check")
                else:
                    messagebox.showinfo("Warning", "Link Of Audio Has To Be Entried!!!")

        window.geometry('1000x400')
        B1 = Entry(window, width=30, font=('Arial', 15))
        B1.grid(row=3, column=1, padx=20, pady=20, sticky="W")
        B2 = Entry(window, width=30, font=('Arial', 15))
        B2.grid(row=4, column=1, padx=20, pady=20, sticky="W")
        L1 = Label(window, text="Please Entry Your Link: ", width=25, font=('Arial', 15))
        L1.grid(row=3, column=0, sticky="W")
        L2 = Label(window, text="Please Choose Place In PC: ", width=25, font=('Arial', 15))
        L2.grid(row=4, column=0, sticky="W")
        B3 = Button(window, text="Download", command=download, font=("arial", 25), background='green')
        B3.grid(row=5, column=0)
    window= tkinter.Tk()
    window.geometry('520x160')
    window.title("Youtube Downloader")
    window.config(background='blue')
    menubar= Menu()
    L=Label(window,text="Welcome in my Youtube Downloader",font=('Arial',20),background='orange')
    L.grid(row=0,column=0,padx=20,pady=20)
    filemenu = Menu(menubar, tearoff=0, background='#ffcc99', foreground='black')
    filemenu.add_command(label="Download only Audio",command=Download_only_song)
    filemenu.add_command(label="Download full Movie",command=Download_full)
    filemenu.add_separator()
    filemenu.add_command(label="Quit",command=window.destroy)
    menubar.add_cascade(label="Options",menu=filemenu)
    window.config(menu=menubar)
    window.mainloop()
Downloader()