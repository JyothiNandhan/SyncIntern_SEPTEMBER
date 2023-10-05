from tkinter import *
import pyshorteners
from pyperclip import *
window=Tk()
window.title("URL-Shortener")
window.geometry("550x550")
window.config(bg="cyan")


def short():
    
    if short_Url.get():
        
        short_Url.delete(0,END)
    if url_entry.get():
        url=pyshorteners.Shortener().tinyurl.short(url_entry.get())
        short_Url.insert(END,url)


def copy_url():
    var=short_Url.get()
    copy(var)




head=Label(window,text="URL-Shortener",font=("Helvetica",25,"bold"),bg="cyan")
head.pack()

url_label=Label(window,text="Enter the URL to be shortened:",font=("Arial",15,"bold"),bg="cyan")
url_label.pack(pady=30)

url_entry=Entry(window,font=("Helvetica",25))
url_entry.pack(padx=20)

my_button=Button(window,text="Shorten",font=("Arial",15,"bold"),command=short,bg="cyan")
my_button.pack(pady=20)

Short_Label=Label(window,text="The Shortened Label:",font=("Helvetica",25),bg="cyan")
Short_Label.pack(pady=20)

short_Url=Entry(window,font=("Helvetica",15),width=35,)
short_Url.pack(padx=20)

copy1=Button(window,text="copy",font=("Helvetica",25),command=copy_url,bg="cyan")
copy1.pack(pady=20)



window.mainloop()