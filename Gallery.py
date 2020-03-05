import sys
import os
from tkinter import *
import GalleryGUI
import AdminLogin
def Show(data,gall):
        try:
                pc=0
                for a in range(0,3):
                    for b in range(0,3):
                        strg=data[pc]
                        strg=strg.replace("\n","")
                        if pc==0:
                            one=strg
                            photo1 = PhotoImage(file =strg)
                            butt0=Button(gall,image=photo1,bd=0,highlightbackground="white", highlightthickness=2,width=200,height=115,command=lambda:[gall.destroy() & GalleryGUI.ExpandImg(one) ])
                            butt0.grid(row=a,column=b)
                        elif pc==1:
                            two=strg
                            photo2 = PhotoImage(file =strg)
                            butt1=Button(gall,image=photo2,bd=0,highlightbackground="white", highlightthickness=2,width=200,height=115,command=lambda:[gall.destroy() & GalleryGUI.ExpandImg(two) ])
                            butt1.grid(row=a,column=b)
                        elif pc==2:
                            three=strg
                            photo3= PhotoImage(file =strg)
                            butt2=Button(gall,image=photo3,bd=0,highlightbackground="white", highlightthickness=2,width=200,height=115,command=lambda:[gall.destroy() & GalleryGUI.ExpandImg(three) ])
                            butt2.grid(row=a,column=b)
                        elif pc==3:
                            four=strg
                            photo4 = PhotoImage(file =strg)
                            butt3=Button(gall,image=photo4,bd=0,highlightbackground="white", highlightthickness=2,width=200,height=115,command=lambda:[gall.destroy() & GalleryGUI.ExpandImg(four) ])
                            butt3.grid(row=a,column=b)
                        elif pc==4:
                            five=strg
                            photo5 = PhotoImage(file =strg)
                            butt4=Button(gall,image=photo5,bd=0,highlightbackground="white", highlightthickness=2,width=200,height=115,command=lambda:[gall.destroy() & GalleryGUI.ExpandImg(five) ])
                            butt4.grid(row=a,column=b)
                        elif pc==5:
                            six=strg
                            photo6 = PhotoImage(file =strg)
                            butt5=Button(gall,image=photo6,bd=0,highlightbackground="white", highlightthickness=2,width=200,height=115,command=lambda:[gall.destroy() & GalleryGUI.ExpandImg(six) ])
                            butt5.grid(row=a,column=b)
                        elif pc==6:
                            seven=strg
                            photo7 = PhotoImage(file =strg)
                            butt6=Button(gall,image=photo7,bd=0,highlightbackground="white", highlightthickness=2,width=200,height=115,command=lambda:[gall.destroy() & GalleryGUI.ExpandImg(seven) ])
                            butt6.grid(row=a,column=b)
                        elif pc==7:
                            eight=strg
                            photo8 = PhotoImage(file =strg)
                            butt7=Button(gall,image=photo8,bd=0,highlightbackground="white", highlightthickness=2,width=200,height=115,command=lambda:[gall.destroy() & GalleryGUI.ExpandImg(eight) ])
                            butt7.grid(row=a,column=b)
                        elif pc==8:
                            nine=strg
                            photo9 = PhotoImage(file =strg)
                            butt8=Button(gall,image=photo9,bd=0,highlightbackground="white", highlightthickness=2,width=200,height=115,command=lambda:[gall.destroy() & GalleryGUI.ExpandImg(nine) ])
                            butt8.grid(row=a,column=b)
                        b+=1
                        pc+=1
                    a+=1
        except IndexError:
                pass
        Button(gall,text="BACK",bg="#d8512f",bd=0,highlightbackground="white", highlightthickness=2,width=20,command=lambda:[gall.destroy() & AdminLogin.AdminOption()]).grid(row=3,column=1)
        gall.mainloop()
def GalleryShow():      
    gall=Tk()
    gall.config(bg="white")
    gall.geometry("600x440+25+0")
    gall.title("GALLERY")
    fname="Gallery.txt"
    data = []
    lines=9
    num_lines = 0
    with open(fname) as f:
        for line in f:
            num_lines += 1
        if num_lines<=9:
            with open (fname) as f:
                data.extend(f.readlines())
                Show(data,gall)
        else:
            bufsize = 8192
            fsize = os.stat(fname).st_size
            iter = 0
            with open(fname) as f:
                if bufsize > fsize:
                        bufsize = fsize-1
                        x=[]
                        while True:
                                iter+=1
                                f.seek(fsize-bufsize*iter)
                                data.extend(f.readlines())
                                if len(data) >= lines or f.tell() == 0:
                                        x.extend(data[-lines:])
                                        Show(x,gall)
                                        break
