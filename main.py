from atbash import *
from scitala import *
from polybius import *
from caesar import *
from grons import *
from vigen import *
from rish import *
from alb import *
from vernam import *
from hill import *
from playfair import *
from cordan import *
from analysisfreq import *
from gamma import *
from analysisPOLI import *
from DES_menu import *
from GOST_menu import *


def main():
    menuW = Tk()
    menuW.title("Криптография Крылова А В")
    menuW.geometry("501x265+421+238")
    menuW.configure(background="#ffcece")

    Atbash = Button(menuW, command=atbash)
    Atbash.place(relx=0.04, rely=0.053, height=64, width=107)
    Atbash.configure(background="#ffffff")
    Atbash.configure(borderwidth="3")
    Atbash.configure(font="-family {Open Sans Light} -size 14 -weight bold")
    Atbash.configure(foreground="#000000")
    Atbash.configure(text='''Атбаш''')
    Atbash.configure(cursor="hand2")

    Scitala = Button(menuW, command=scitala)
    Scitala.place(relx=0.279, rely=0.053, height=64, width=107)
    Scitala.configure(background="#ffffff")
    Scitala.configure(borderwidth="3")
    Scitala.configure(font="-family {Open Sans Light} -size 14 -weight bold")
    Scitala.configure(foreground="#000000")
    Scitala.configure(text='''Сцитала''')
    Scitala.configure(cursor="hand2")

    Button5 = Button(menuW, command=cordan)
    Button5.place(relx=0.04, rely=0.366, height=64, width=107)
    Button5.configure(background="#ffffff")
    Button5.configure(borderwidth="3")
    Button5.configure(font="-family {Open Sans Light} -size 14 -weight bold")
    Button5.configure(foreground="#000000")
    Button5.configure(text='''Р.Кордано''')

    Rish = Button(menuW, command=rish)
    Rish.place(relx=0.279, rely=0.366, height=64, width=107)
    Rish.configure(background="#ffffff")
    Rish.configure(borderwidth="3")
    Rish.configure(font="-family {Open Sans Light} -size 14 -weight bold")
    Rish.configure(foreground="#000000")
    Rish.configure(text='''Ришелье''')
    Rish.configure(cursor="hand2")

    Polybius = Button(menuW, command=polybius)
    Polybius.place(relx=0.519, rely=0.053, height=64, width=107)
    Polybius.configure(background="#ffffff")
    Polybius.configure(borderwidth="3")
    Polybius.configure(font="-family {Open Sans Light} -size 14 -weight bold")
    Polybius.configure(foreground="#000000")
    Polybius.configure(text='''Квадрат П.''')
    Polybius.configure(cursor="hand2")

    Caesar = Button(menuW, command=caesar)
    Caesar.place(relx=0.758, rely=0.053, height=64, width=107)
    Caesar.configure(background="#ffffff")
    Caesar.configure(borderwidth="3")
    Caesar.configure(font="-family {Open Sans Light} -size 14 -weight bold")
    Caesar.configure(foreground="#000000")
    Caesar.configure(text='''Цезарь''')
    Caesar.configure(cursor="hand2")


    Vigen = Button(menuW, command=vigen)
    Vigen.place(relx=0.04, rely=0.694, height=64, width=107)
    Vigen.configure(background="#ffffff")
    Vigen.configure(borderwidth="3")
    Vigen.configure(font="-family {Open Sans Light} -size 14 -weight bold")
    Vigen.configure(foreground="#000000")
    Vigen.configure(text='''Виженер''')
    Vigen.configure(cursor="hand2")

    Grons = Button(menuW, command=grons)
    Grons.place(relx=0.758, rely=0.366, height=64, width=107)
    Grons.configure(background="#ffffff")
    Grons.configure(borderwidth="3")
    Grons.configure(font="-family {Open Sans Light} -size 10 -weight bold")
    Grons.configure(foreground="#000000")
    Grons.configure(text=''' Гронсфельд''')
    Grons.configure(cursor="hand2")

    Button12 = Button(menuW, command=vernam)
    Button12.place(relx=0.758, rely=0.694, height=64, width=107)
    Button12.configure(background="#ffffff")
    Button12.configure(borderwidth="3")
    Button12.configure(font="-family {Open Sans Light} -size 14 -weight bold")
    Button12.configure(foreground="#000000")
    Button12.configure(text='''Вернам''')

    Button11 = Button(menuW, command=hill)
    Button11.place(relx=0.519, rely=0.694, height=64, width=107)
    Button11.configure(background="#ffffff")
    Button11.configure(borderwidth="3")
    Button11.configure(font="-family {Open Sans Light} -size 14 -weight bold")
    Button11.configure(foreground="#000000")
    Button11.configure(text='''Хилл''')

    Alb = Button(menuW, command=alb)
    Alb.place(relx=0.519, rely=0.366, height=64, width=107)
    Alb.configure(background="#ffffff")
    Alb.configure(borderwidth="3")
    Alb.configure(font="-family {Open Sans Light} -size 14 -weight bold")
    Alb.configure(foreground="#000000")
    Alb.configure(text='''Альберти''')
    Alb.configure(cursor="hand2")

    Button10 = Button(menuW, command=playfair)
    Button10.place(relx=0.279, rely=0.694, height=64, width=107)
    Button10.configure(background="#ffffff")
    Button10.configure(borderwidth="3")
    Button10.configure(font="-family {Open Sans Light} -size 14 -weight bold")
    Button10.configure(foreground="#000000")
    Button10.configure(text='''Плейфер''')



    menuW2 = Tk()
    menuW2.geometry("472x195+451+332")
    menuW2.minsize(120, 1)
    menuW2.maxsize(1444, 941)
    menuW2.resizable(1, 1)
    menuW2.title("Криптография Крылова А В")
    menuW2.configure(background="#e6fdff")

    Button1_2 = Button(menuW2, command=freq)
    Button1_2.place(relx=0.042, rely=0.154, height=54, width=127)
    Button1_2.configure(activebackground="beige")
    Button1_2.configure(activeforeground="#000000")
    Button1_2.configure(background="#e9e9e9")
    Button1_2.configure(compound='left')
    Button1_2.configure(disabledforeground="#a3a3a3")
    Button1_2.configure(foreground="#000000")
    Button1_2.configure(highlightbackground="#d9d9d9")
    Button1_2.configure(highlightcolor="black")
    Button1_2.configure(pady="0")
    Button1_2.configure(text='''Част. анализ''')

    Button2_2 = Button(menuW2, command=gamma)
    Button2_2.place(relx=0.36, rely=0.154, height=54, width=127)
    Button2_2.configure(activebackground="beige")
    Button2_2.configure(activeforeground="#000000")
    Button2_2.configure(background="#e9e9e9")
    Button2_2.configure(compound='left')
    Button2_2.configure(disabledforeground="#a3a3a3")
    Button2_2.configure(foreground="#000000")
    Button2_2.configure(highlightbackground="#d9d9d9")
    Button2_2.configure(highlightcolor="black")
    Button2_2.configure(pady="0")
    Button2_2.configure(text='''Гамма''')

    Button3_2 = Button(menuW2, command=analysisMENU)
    Button3_2.place(relx=0.678, rely=0.154, height=54, width=127)
    Button3_2.configure(activebackground="beige")
    Button3_2.configure(activeforeground="#000000")
    Button3_2.configure(background="#e9e9e9")
    Button3_2.configure(compound='left')
    Button3_2.configure(disabledforeground="#a3a3a3")
    Button3_2.configure(foreground="#000000")
    Button3_2.configure(highlightbackground="#d9d9d9")
    Button3_2.configure(highlightcolor="black")
    Button3_2.configure(pady="0")
    Button3_2.configure(text='''Полиалф. анализ''')

    Button4_2 = Button(menuW2, command=desM)
    Button4_2.place(relx=0.191, rely=0.513, height=54, width=137)
    Button4_2.configure(activebackground="beige")
    Button4_2.configure(activeforeground="#000000")
    Button4_2.configure(background="#e9e9e9")
    Button4_2.configure(compound='left')
    Button4_2.configure(disabledforeground="#a3a3a3")
    Button4_2.configure(foreground="#000000")
    Button4_2.configure(highlightbackground="#d9d9d9")
    Button4_2.configure(highlightcolor="black")
    Button4_2.configure(pady="0")
    Button4_2.configure(text='''DES''')

    Button5_2 = Button(menuW2, command=gostM)
    Button5_2.place(relx=0.53, rely=0.513, height=54, width=137)
    Button5_2.configure(activebackground="beige")
    Button5_2.configure(activeforeground="#000000")
    Button5_2.configure(background="#e9e9e9")
    Button5_2.configure(compound='left')
    Button5_2.configure(disabledforeground="#a3a3a3")
    Button5_2.configure(foreground="#000000")
    Button5_2.configure(highlightbackground="#d9d9d9")
    Button5_2.configure(highlightcolor="black")
    Button5_2.configure(pady="0")
    Button5_2.configure(text='''ГОСТ''')

    menuW.mainloop()
    menuW2.mainloop()

if __name__ == "__main__":
    main()
