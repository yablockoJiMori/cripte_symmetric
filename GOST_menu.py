from GOST_file import *
from GOST_buf import *

def gostM():
    desmW=Tk()
    desmW.geometry("288x92+581+324")
    desmW.minsize(120, 1)
    desmW.maxsize(1444, 941)
    desmW.resizable(1, 1)
    desmW.title("desmWlevel 0")
    desmW.configure(background="#e6fdff")

    Button1 = Button(desmW, command=GOSTb)
    Button1.place(relx=0.556, rely=0.326, height=34, width=97)
    Button1.configure(activebackground="beige")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#e9e9e9")
    Button1.configure(compound='left')
    Button1.configure(disabledforeground="#a3a3a3")
    Button1.configure(foreground="#000000")
    Button1.configure(highlightbackground="#d9d9d9")
    Button1.configure(highlightcolor="black")
    Button1.configure(pady="0")
    Button1.configure(text='''из буфера''')

    Button2 = Button(desmW, command=GOSTf)
    Button2.place(relx=0.139, rely=0.326, height=34, width=97)
    Button2.configure(activebackground="beige")
    Button2.configure(activeforeground="#000000")
    Button2.configure(background="#e9e9e9")
    Button2.configure(compound='left')
    Button2.configure(disabledforeground="#a3a3a3")
    Button2.configure(foreground="#000000")
    Button2.configure(highlightbackground="#d9d9d9")
    Button2.configure(highlightcolor="black")
    Button2.configure(pady="0")
    Button2.configure(text='''файл''')

