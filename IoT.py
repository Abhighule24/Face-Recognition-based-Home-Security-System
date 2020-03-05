import MotionSense
from tkinter import *
import AdminLogin
def Enter():
    home = Tk()
    home.config(bg="white")
    home.geometry("600x400+25+0")
    home.title("VIRABHI")
    photo = PhotoImage(file = "IOT_HOME.png")
    Label(home,text="WELCOME TO IOT BASED HOME SECURITY SYSTEM",bg="white",font="Calibri 16 bold").pack(fill=BOTH)
    Button(home,width=600,height=300,bd=0,image=photo,command=lambda:[home.destroy() & MotionSense.Motion()]).pack()
    Button(home,text="ADMIN LOGIN",relief=FLAT,bg="#2D80B7",fg="white",width=200,command=lambda:[home.destroy() & AdminLogin.AdminScr()]).pack(padx=25, pady=10, side=LEFT)
    home.mainloop()
