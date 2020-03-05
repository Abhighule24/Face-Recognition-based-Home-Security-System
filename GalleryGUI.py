from tkinter import *
import Gallery
def ExpandImg(strg):
        expx=Tk()
        expx.config(bg="white")
        expx.geometry("600x400+25+0")
        expx.title(strg)
        expx.geometry("600x400+25+0")
        photo = PhotoImage(file =strg)
        Label(expx,image=photo,bd=0,highlightbackground="white", highlightthickness=2,width=600,height=350).pack()
        Button(expx,text="BACK",bg="#d8512f",bd=0,highlightbackground="white", highlightthickness=2,width=20,command=lambda:[expx.destroy() & Gallery.GalleryShow()]).pack(pady=5,padx=5)
        expx.mainloop()

