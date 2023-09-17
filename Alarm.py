from tkinter import*
import time
import datetime
from tkinter import messagebox
from playsound import playsound

win=Tk()
win.title("Alarm Clock")
win.geometry("500x300")
win.config(bg="orange")




def Alarm():
   global Hours,Minutes
   h=int(Hours.get())
   m=int(Minutes.get())

   while(1):
       if(h==datetime.datetime.now().hour and m==datetime.datetime.now().minute):
           playsound("C:\\Users\\LENOVO\\Desktop\\Nandhan_p\\Music\\Nice.mp3")
           messagebox.showinfo("Alarm","Please Wake up!")
           break
    
   

      

                   

def get_time():
    timeVar=time.strftime("%H:%M:%S")
    PresentTime.config(text=timeVar)
    PresentTime.after(200,get_time)

def set_alarm():
   
    window=Toplevel()
    window.geometry("600x400")
    window.config(bg="#37FD12")
    global Hours,Minutes
    L1=Label(window,text="Enter the Hours to set the Alarm",font=("Arial",20,"bold"))
    L1.place(x="50",y="10")

    Hours=Entry(window,width=10,font=("Arial",25,"italic"))
    Hours.place(x="80",y="50")

    L2=Label(window,text="Enter the minutes to set the Alarm",font=("Arial",20,"bold"))
    L2.place(x="50",y="150")

    Minutes=Entry(window,width=10,font=("Arial",25,"italic"))
    Minutes.place(x="80",y="190")

    Add_alarm=Button(window,text=" Start",font=("Times New Roman",15,"bold"),bg="orange",command=Alarm)
    Add_alarm.place(x="200",y="300")

    # dismiss_alarm=Button(window,text=" Dismiss",font=("Times New Roman",15,"bold"),bg="orange",command=lambda:(window.destroy()))
    # dismiss_alarm.place(x="300",y="300")




heading=Label(win,text="Alarm Clock",font=("Times New Roman",30,"bold"),bg="orange",fg="black")
heading.place(x="150",y="10")

PresentTime=Label(win,font=("Times New Roman",80,"bold"),bg="black",fg="#37FD12")
PresentTime.place(x="50",y="100")

setAlarm=Button(win,text="Set Alarm",font=("Times New Roman",20,"bold"),command=set_alarm)
setAlarm.place(x="200",y="250")

get_time()


win.mainloop()
