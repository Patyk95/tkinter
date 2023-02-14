import pytube.exceptions
from pytube import YouTube
import tkinter
from tkinter import *
from tkinter import messagebox
fileSizeInBytes = 0
MaxFileSize = 0
def Downloader():
    def Download_full():
        def download():
            try:
                if len(B1.get())>1:
                    link =B1.get()
                    yt= YouTube(link)
                    title= yt.title
                    view= yt.views
                    ys = yt.streams.get_highest_resolution()
                    ys.download()
                    messagebox.showinfo("Done",f"You have downloaded {title}, which has {view} views in Youtube")
                else:
                    messagebox.showerror("Error","Pleace copy link")
            except pytube.exceptions.RegexMatchError:
                    messagebox.showerror("Error","Your link is incorrect")
            finally:
                    messagebox.showinfo("INFO", "THANKS FOR USING MY YOUTUBE DOWNLOADER")

        window.geometry('1000x250')
        B1=Entry(window,width=30,font=('Arial',15))
        B1.grid(row=3,column=1,padx=20,pady=20,sticky="W")
        L1=Label(window,text="Please Entry Your Link: ",width=25,font=('Arial',15))
        L1.grid(row=3,column=0,sticky="W")
        B3=Button(window,text="Download",command=download,font=("arial",25),background='green')
        B3.grid(row=7,column=0,pady=20,padx=20)
    window= tkinter.Tk()
    window.geometry('520x160')
    window.title("Youtube Downloader")
    window.config(background='blue')
    menubar= Menu()
    L=Label(window,text="Welcome in my Youtube Downloader",font=('Arial',20),background='orange')
    L.grid(row=0,column=0,padx=20,pady=20)
    filemenu = Menu(menubar, tearoff=0, background='#ffcc99', foreground='black')
    filemenu.add_command(label="Download full Movie",command=Download_full)
    filemenu.add_separator()
    filemenu.add_command(label="Quit",command=window.destroy)
    menubar.add_cascade(label="Options",menu=filemenu)
    window.config(menu=menubar)
    window.mainloop()
Downloader()