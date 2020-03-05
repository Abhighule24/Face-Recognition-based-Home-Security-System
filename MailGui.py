from tkinter import *
import IoT
import AdminLogin
def MailLog(x):
    mailer=Tk()
    mailer.config(bg="white")
    mailer.geometry("420x225+120+80")
    mailer.title("IoT")
    Label(mailer,text=x,bg="white").pack(fill=BOTH, padx=10,pady=10)
    Button(mailer,text="BACK",bg="#d8512f",fg="white",width=20,command=lambda:[mailer.destroy() & AdminLogin.AdminOption()]).pack(padx=10,pady=5)
    mailer.mainloop()
