from tkinter import *
from tkinter import messagebox
import MailLog
import Gallery
import SOS_SMS
import IoT
def AdminScr():
    logscr=Tk()
    logscr.geometry("300x220+170+100")
    logscr.title("Admin Login")
    logscr.configure(background='white')
    userid = StringVar()
    password = StringVar()
    def Verify():
        x=userid.get()
        y=password.get()
        if x=="admin" and y=="12345":
            logscr.destroy()
            AdminOption()
        else:
            messagebox.showerror("Alert", "LOGIN UNSUCCESSFUL")

    Label(text="LOGIN",bg='white',width="300",height="2").pack()
    Label(text="USERNAME",bg='white',width="300",height="2").pack()
    Entry(logscr,bg='white',textvariable=userid,show= '*').pack()
    Label(text="PASSWORD",bg='white',width="300",height="2").pack()
    Entry(logscr,bg='white',textvariable=password,show= '*').pack()
    Button(logscr,text="LOGIN",fg="white",bg="#2D80B7",width=15,command=Verify).pack(pady=5)
    Button(logscr,text="BACK",fg="white",bg="#d8512f",width=15,command=lambda:[logscr.destroy() & IoT.Enter()]).pack(pady=5)
    logscr.mainloop()
def AdminOption():
    Admop=Tk()
    Admop.geometry("300x200+170+100")
    Admop.title("Admin Login")
    Admop.configure(background='white')
    Button(Admop,text="SOS MESSAGE",relief=FLAT,bg="#2D80B7",fg="white",width=15,command=SOS_SMS.SendMsg).pack(pady=10)#padx=25, pady=10, side=LEFT)
    Button(Admop,text="GALLERY",relief=FLAT,bg="#2D80B7",fg="white",width=15,command=lambda:[Admop.destroy() & Gallery.GalleryShow()]).pack(pady=10)#padx=25, pady=10, side=LEFT)
    Button(Admop,text="MAIL LOG",relief=FLAT,bg="#2D80B7",fg="white",width=15,command=lambda:[Admop.destroy() & MailLog.Print_Last_Lines()]).pack(pady=10)#padx=25, pady=10, side=LEFT)
    Button(Admop,text="BACK",relief=FLAT,bg="#d8512f",fg="white",width=15,command=lambda:[Admop.destroy() & IoT.Enter()]).pack(pady=10)#padx=25, pady=10, side=LEFT)
    Admop.mainloop()
