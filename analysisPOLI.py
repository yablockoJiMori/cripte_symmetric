from tkinter import *
from anIndex import *
from anAutocor import *
from anKasis import *
def analysisMENU():


    analysisPOLIW =Tk()
    analysisPOLIW.geometry("437x109+443+316")
    analysisPOLIW.minsize(120, 1)
    analysisPOLIW.maxsize(1444, 941)
    analysisPOLIW.resizable(1, 1)
    analysisPOLIW.title("Анализ полиалфавитных шифров")
    analysisPOLIW.configure(background="#e6fdff")



    indB = Button(analysisPOLIW, command=anIndex)
    indB.place(relx=0.046, rely=0.275, height=54, width=127)
    indB.configure(activebackground="beige")
    indB.configure(activeforeground="#000000")
    indB.configure(background="#e9e9e9")
    indB.configure(compound='left')
    indB.configure(disabledforeground="#a3a3a3")
    indB.configure(foreground="#000000")
    indB.configure(highlightbackground="#d9d9d9")
    indB.configure(highlightcolor="black")
    indB.configure(pady="0")
    indB.configure(text='''Индекс совпадений''')

    autoB = Button(analysisPOLIW, command=anAuto)
    autoB.place(relx=0.366, rely=0.275, height=54, width=127)
    autoB.configure(activebackground="beige")
    autoB.configure(activeforeground="#000000")
    autoB.configure(background="#e9e9e9")
    autoB.configure(compound='left')
    autoB.configure(disabledforeground="#a3a3a3")
    autoB.configure(foreground="#000000")
    autoB.configure(highlightbackground="#d9d9d9")
    autoB.configure(highlightcolor="black")
    autoB.configure(pady="0")
    autoB.configure(text='''Автокорреляция''')

    kasakiB = Button(analysisPOLIW, command=anKas)
    kasakiB.place(relx=0.686, rely=0.275, height=54, width=127)
    kasakiB.configure(activebackground="beige")
    kasakiB.configure(activeforeground="#000000")
    kasakiB.configure(background="#e9e9e9")
    kasakiB.configure(compound='left')
    kasakiB.configure(disabledforeground="#a3a3a3")
    kasakiB.configure(foreground="#000000")
    kasakiB.configure(highlightbackground="#d9d9d9")
    kasakiB.configure(highlightcolor="black")
    kasakiB.configure(pady="0")
    kasakiB.configure(text='''Тест Казиски''')

    analysisPOLIW.mainloop()