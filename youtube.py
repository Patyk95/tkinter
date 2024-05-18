import pytube.exceptions
from pytube import YouTube
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk

fileSizeInBytes = 0
MaxFileSize = 0

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

def Downloader():
    def download():
        try:
            if len(B2.get())>1:
                link =B2.get()
                yt= YouTube(link)
                title= yt.title
                view= yt.views
                ys = yt.streams.get_highest_resolution()
                ys.download()
                messagebox.showinfo("Done",f"You Have Downloaded {title}, Which Has {view} Views In Youtube")
                messagebox.showinfo("INFO", "Thanks For Using My Program")
            elif len(B2.get())<=1:
                messagebox.showerror("Error","Pleace Pass Link")
        except pytube.exceptions.RegexMatchError:
                messagebox.showerror("Error","Your Link Is Incorrect")

    window = ctk.CTk()
    B2=ctk.CTkEntry(window,width=500,font=('Arial',15))
    B2.grid(row=3,column=0,padx=20,pady=20,sticky="W")
    L2=ctk.CTkLabel(window,text="Please Pass Your Link ",width=25,font=('Arial',30))
    L2.grid(row=2,padx=20,pady=20,column=0,sticky="n")   
    window.geometry('520x460')
    window.title("Youtube Downloader")
    L1=ctk.CTkLabel(window,text="Welcome in my Youtube Downloader",font=('ariel',30))
    L1.grid(row=1,column=0,padx=20,pady=20)
    B1=ctk.CTkButton(window,text = "DOWNLOAD",command=download,font=("ariel",30))
    B1.grid(row=6,column=0)
    window.mainloop()
Downloader()