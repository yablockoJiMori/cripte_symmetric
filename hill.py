from tkinter import *
from tkinter.constants import *
from tkinter import messagebox
import numpy as np
import sympy as sp
def hill():
    alfavit = "^u&ИЙ5OЬz+QRZPq№|aя,SБ}СуwнA_*азgЕX19]yтлР;G-шj?ГъdЧёHхТ`ЯЪцщpвМ>vюп#C6MmiЩЗО!Уоr.ПсФ4 ьч2ХЛIм3=ВШY~(DЁ$киы{cnдАsКйEFW0ДЮxoеlNЭK@\LэhBJ[:'T%bгбНkUр78ЫжtЦe<фV/Жf)\n\""
    alfavit = list(alfavit)
    def keyCr():
        openSTR = openText.get(1.0, END)
        openSTR=openSTR[:-1]
        keyMat = [[0] * len(openSTR) for i in range(len(openSTR))]
        key = ""
        for i in range(len(openSTR)):
            for j in range(len(openSTR)):
                keyMat[i][j] = np.random.randint(0, 163)
                key = key + alfavit[keyMat[i][j]]

        keyGrons.delete(0, END)
        keyGrons.insert(0, key)


    def hillE():
        openSTR = openText.get(1.0, END)
        openSTR=openSTR[:-1]
        key = keyGrons.get()
        keyMat = [[0] * len(openSTR) for i in range(len(openSTR))]
        for i in range(len(openSTR)):
            for j in range(len(openSTR)):
                letter = key[i*len(openSTR)+j]
                keyMat[i][j] = alfavit.index(letter)
        keyMat = sp.Matrix(keyMat)
        if len(key) != len(openSTR) * len(openSTR) or keyMat.det() % 163 == 0:
            messagebox.showerror('Ошибка', 'Неверный ключ.')
        else:
            matrixSTR = [[0] * 1 for i in range(len(openSTR))]
            for i in range(len(openSTR)):
                letter = openSTR[i]
                matrixSTR[i][0] = alfavit.index(letter)


            matrixSTR = sp.Matrix(matrixSTR)
            total = keyMat * matrixSTR

            total = np.array(total)
            for i in range(len(total)):
                total[i] = total[i] % 163

            cipherSTR = ""
            for i in total:
                cipherSTR = cipherSTR + alfavit[int(i)]

            cipherText.delete(1.0, END)
            cipherText.insert(1.0, cipherSTR)


    def hillD():
        openSTR = cipherText.get(1.0, END)
        openSTR = openSTR[:-1]
        key = keyGrons.get()
        keyMat = [[0] * len(openSTR) for i in range(len(openSTR))]
        for i in range(len(openSTR)):
            for j in range(len(openSTR)):
                letter = key[i*len(openSTR)+j]
                keyMat[i][j] = alfavit.index(letter)
        keyMat = sp.Matrix(keyMat)
        if len(key) != len(openSTR) * len(openSTR) or keyMat.det() % 163 == 0:
            messagebox.showerror('Ошибка', 'Неверный ключ.')
        else:
            keyMatR = np.array(sp.Matrix(keyMat).inv_mod(len(alfavit)))

            matrixSTR = [[0] * 1 for i in range(len(openSTR))]
            for i in range(len(openSTR)):
                letter = openSTR[i]
                matrixSTR[i][0] = alfavit.index(letter)

            totalf = np.matmul(keyMatR, matrixSTR)

            for i in range(len(totalf)):
                totalf[i] = totalf[i] % 163

            cipherSTR = ""
            for i in totalf:
                cipherSTR = cipherSTR + alfavit[int(i)]

            openText.delete(1.0, END)
            openText.insert(1.0, cipherSTR)


    def rishI():
        messagebox.showinfo('О Шифре Ришелье', 'Ожидается')

    rishW = Tk()
    rishW.geometry("716x263+322+179")
    rishW.title("Шифр Хилла")
    rishW.configure(background="#ffcece")

    openText = Text(rishW)
    openText.place(relx=0.029, rely=0.3, relheight=0.612, relwidth=0.37)
    openText.configure(background="white")
    openText.configure(borderwidth="2")
    openText.configure(font="-family {@Malgun Gothic} -size 13")
    openText.configure(foreground="black")

    cipherText = Text(rishW)
    cipherText.place(relx=0.601, rely=0.3, relheight=0.612, relwidth=0.37)
    cipherText.configure(background="white")
    cipherText.configure(borderwidth="2")
    cipherText.configure(font="-family {@Malgun Gothic} -size 13")
    cipherText.configure(foreground="black")

    encryptPolybius = Button(rishW, command=hillE)
    encryptPolybius.place(relx=0.419, rely=0.305, height=34, width=115)
    encryptPolybius.configure(background="#ffffff")
    encryptPolybius.configure(borderwidth="3")
    encryptPolybius.configure(cursor="hand2")
    encryptPolybius.configure(font="-family {@Malgun Gothic} -size 10")
    encryptPolybius.configure(foreground="#000000")
    encryptPolybius.configure(text='''Зашифровать ->''')

    decipherPolybius = Button(rishW, command=hillD)
    decipherPolybius.place(relx=0.419, rely=0.455, height=34, width=114)
    decipherPolybius.configure(background="#ffffff")
    decipherPolybius.configure(borderwidth="3")
    decipherPolybius.configure(cursor="hand2")
    decipherPolybius.configure(font="-family {@Malgun Gothic} -size 10")
    decipherPolybius.configure(foreground="#000000")
    decipherPolybius.configure(text='''<-Расшифровать''')

    keyButton = Button(rishW, command=keyCr)
    keyButton.place(relx=0.419, rely=0.605, height=34, width=113)
    keyButton.configure(background="#ffffff")
    keyButton.configure(borderwidth="3")
    keyButton.configure(cursor="hand2")
    keyButton.configure(font="-family {@Malgun Gothic} -size 10")
    keyButton.configure(foreground="#000000")
    keyButton.configure(text='''Ключ''')

    headGrons = Label(rishW)
    headGrons.place(relx=0.279, rely=0.075, height=52, width=341)
    headGrons.configure(background="#ffcece")
    headGrons.configure(font="-family {Open Sans Light} -size 20 -weight bold")
    headGrons.configure(foreground="#000000")
    headGrons.configure(text='''Шифр Хилла''')

    information = Button(rishW, command=rishI)
    information.place(relx=0.95, rely=0.038, height=24, width=27)
    information.configure(background="#ffffff")
    information.configure(borderwidth="3")
    information.configure(compound='left')
    information.configure(cursor="question_arrow")
    information.configure(font="-family {Segoe UI} -size 11")
    information.configure(foreground="#000000")
    information.configure(text='''?''')

    headChar = Label(rishW)
    headChar.place(relx=0.412, rely=0.865, height=21, width=134)
    headChar.configure(background="#ffcece")
    headChar.configure(disabledforeground="#a3a3a3")
    headChar.configure(font="-family {@Malgun Gothic} -size 8")
    headChar.configure(foreground="#000000")
    headChar.configure(text='''Ключ''')

    keyGrons = Entry(rishW)
    keyGrons.place(relx=0.419, rely=0.771, height=30, relwidth=0.159)
    keyGrons.configure(background="white")
    keyGrons.configure(borderwidth="2")
    keyGrons.configure(font="-family {@Malgun Gothic} -size 10")
    keyGrons.configure(foreground="#000000")



    rishW.mainloop()