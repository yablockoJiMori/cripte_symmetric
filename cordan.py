from tkinter import *
from tkinter.constants import *
from tkinter import messagebox
import tkinter.ttk as ttk
import re
import numpy as np
from random import randint


def cordan():
    rubbish='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    def genKey():
        size = sizeKey.get()
        if not size.isdigit():
            messagebox.showerror('Ошибка', 'Неверный размер.')
        else:

            size=int(size)
            if size%2==1:
                messagebox.showerror('Ошибка', 'Неверный размер.')
            else:
                qsize = size // 2
                quarter = np.arange(1, qsize ** 2 + 1)
                quarter = np.reshape(quarter, (qsize, qsize))
                quarters = []
                for i in range(4):
                    quarters.append(np.rot90(quarter, -i))
                down = np.hstack([quarters[3], quarters[2]])
                up = np.hstack([quarters[0], quarters[1]])
                Template = np.vstack([up, down])

                coor = []
                for k in range(1, (size // 2) ** 2 + 1):
                    coorDit = []
                    for i in range(size):
                        for j in range(size):
                            if Template[i][j] == k:
                                coorDit.append([i, j])
                    coor.append(coorDit)

                for k in range(0, (size // 2) ** 2):
                    dit = [0, 1, 2, 3]
                    poin = randint(0, 3)
                    del dit[poin]
                    for i in dit:
                        tmp_coor = coor[k][i]
                        Template[tmp_coor[0]][tmp_coor[1]] = 0

                keySTR=""
                for i in range(size):
                    for j in range(size):
                        keySTR=keySTR+str(Template[i][j])+" "
                        if j == size-1:
                            keySTR = keySTR[:-1]
                            keySTR = keySTR + "\n"
                    if i == size - 1:
                        keySTR = keySTR[:-1]




                keyGrons.delete(1.0, END)
                keyGrons.insert(1.0, keySTR)


    def rishE():
        openSTR = openText.get(1.0, END)
        openSTR = openSTR[:-1]
        size = sizeKey.get()
        size = int(size)
        key = keyGrons.get(1.0, END)
        key = key[:-1]
        if not re.match(r"^\d+( \d+|\n\d+)*$", key):
            messagebox.showerror('Ошибка', 'Неверный ключ1.')
        else:
            key = key.split("\n")
            for i in range(len(key)):
                key[i] = key[i].split(" ")
            sum = 0
            for i in range(len(key)):
                for j in range(len(key[i])):
                    key[i][j] = int(key[i][j])
                    sum += 1
            if sum != (size**2):
                messagebox.showerror('Ошибка', 'Неверный ключ2.')
            else:
                flacSTR = []
                for k in range(1,(size // 2) ** 2+1):
                    flac = 0
                    for i in range(len(key)):
                        for j in range(len(key)):
                            if k == key[i][j]:
                                flac += 1
                    flacSTR.append(flac)
                if flacSTR != [1] * ((size // 2) ** 2):
                    messagebox.showerror('Ошибка', 'Неверный ключ3.')

                else:
                    cipherSTR = ""
                    Grilles = []
                    for i in range(4):
                        Grilles.append(np.rot90(key, -i))


                    MatChit = [[0 for i in range(size)] for j in range(size)]
                    for k in range(4):

                        for let in range(k * ((size // 2) ** 2), k * ((size // 2) ** 2) + ((size // 2) ** 2)):
                            for i in range(size):
                                for j in range(size):
                                    if Grilles[k][i][j] == let % ((size // 2) ** 2) + 1:
                                        if let < len(openSTR):
                                            MatChit[i][j] = openSTR[let]
                                        else:
                                            lan=TCombobox1.get()
                                            if lan=="Без мусора":
                                                MatChit[i][j] = "*"
                                            if lan=="С мусором":
                                                MatChit[i][j] = rubbish[randint(0, len(rubbish) - 1)]
                                        break

                    cipherSTR = MatChit
                    cipherSTR = ""
                    for i in range(size):
                        for j in range(size):
                            cipherSTR = cipherSTR + str(MatChit[i][j]) + " "
                            if j == size - 1:
                                cipherSTR = cipherSTR[:-1]
                                cipherSTR = cipherSTR + "\n"
                        if i == size - 1:
                            cipherSTR = cipherSTR[:-1]

                    cipherText.delete(1.0, END)
                    cipherText.insert(1.0, cipherSTR)

    def rishD():
        openSTR = cipherText.get(1.0, END)
        openSTR = openSTR[:-1]
        size = sizeKey.get()
        size = int(size)
        key = keyGrons.get(1.0, END)
        key = key[:-1]
        if not re.match(r"^\d+( \d+|\n\d+)*$", key):
            messagebox.showerror('Ошибка', 'Неверный ключ1.')
        else:

            key = key.split("\n")
            for i in range(len(key)):
                key[i] = key[i].split(" ")
            sum = 0
            for i in range(len(key)):
                for j in range(len(key[i])):
                    key[i][j] = int(key[i][j])
                    sum += 1
            if sum != (size ** 2):
                messagebox.showerror('Ошибка', 'Неверный ключ2.')
            else:
                flacSTR = []
                for k in range(1, (size // 2) ** 2 + 1):
                    flac = 0
                    for i in range(len(key)):
                        for j in range(len(key)):
                            if k == key[i][j]:
                                flac += 1
                    flacSTR.append(flac)
                if flacSTR != [1] * ((size // 2) ** 2):
                    messagebox.showerror('Ошибка', 'Неверный ключ3.')

                else:
                    cipherSTR = ""
                    Grilles = []
                    for i in range(4):
                        Grilles.append(np.rot90(key, -i))
                    ChMat = [[0 for i in range(size)] for j in range(size)]
                    f=0
                    for i in range(len(ChMat)):
                        for j in range(len(ChMat)):
                            ChMat[i][j] = openSTR[f]
                            f += 2

                    chiSTR = ""
                    for k in range(4):
                        for f in range(((size // 2) ** 2)):
                            for i in range(size):
                                for j in range(size):
                                    if Grilles[k][i][j] == f + 1:
                                        chiSTR = chiSTR + ChMat[i][j]

                    chiSTR = chiSTR.replace("*", '')
                    openText.delete(1.0, END)
                    openText.insert(1.0, chiSTR)

    def rishI():
        messagebox.showinfo('О Шифре Ришелье', 'Ожидается')

    rishW = Tk()
    rishW.geometry("596x450+368+185")
    rishW.title("Шифр Ришелье")
    rishW.configure(background="#e6fdff")

    openText = Text(rishW)
    openText.place(relx=0.05, rely=0.156, relheight=0.342, relwidth=0.29)
    openText.configure(background="white")
    openText.configure(font="TkTextFont")
    openText.configure(foreground="black")
    openText.configure(highlightbackground="#d9d9d9")
    openText.configure(highlightcolor="black")
    openText.configure(insertbackground="black")
    openText.configure(selectbackground="#c4c4c4")
    openText.configure(selectforeground="black")
    openText.configure(wrap="word")

    cipherText = Text(rishW)
    cipherText.place(relx=0.654, rely=0.156, relheight=0.342, relwidth=0.29)
    cipherText.configure(background="white")
    cipherText.configure(cursor="fleur")
    cipherText.configure(font="TkTextFont")
    cipherText.configure(foreground="black")
    cipherText.configure(highlightbackground="#d9d9d9")
    cipherText.configure(highlightcolor="black")
    cipherText.configure(insertbackground="black")
    cipherText.configure(selectbackground="#c4c4c4")
    cipherText.configure(selectforeground="black")
    cipherText.configure(wrap="word")

    keyGrons = Text(rishW)
    keyGrons.place(relx=0.369, rely=0.6, relheight=0.342, relwidth=0.257)
    keyGrons.configure(background="white")
    keyGrons.configure(font="TkTextFont")
    keyGrons.configure(foreground="black")
    keyGrons.configure(highlightbackground="#d9d9d9")
    keyGrons.configure(highlightcolor="black")
    keyGrons.configure(insertbackground="black")
    keyGrons.configure(selectbackground="#c4c4c4")
    keyGrons.configure(selectforeground="black")
    keyGrons.configure(wrap="word")

    sizeKey = Entry(rishW)
    sizeKey.place(relx=0.386, rely=0.422, height=30, relwidth=0.208)
    sizeKey.configure(background="white")
    sizeKey.configure(disabledforeground="#a3a3a3")
    sizeKey.configure(font="TkFixedFont")
    sizeKey.configure(foreground="#000000")
    sizeKey.configure(insertbackground="black")

    encryptPolybius = Button(rishW, command=rishE)
    encryptPolybius.place(relx=0.386, rely=0.156, height=34, width=127)
    encryptPolybius.configure(activebackground="beige")
    encryptPolybius.configure(activeforeground="#000000")
    encryptPolybius.configure(background="#e9e9e9")
    encryptPolybius.configure(compound='left')
    encryptPolybius.configure(disabledforeground="#a3a3a3")
    encryptPolybius.configure(foreground="#000000")
    encryptPolybius.configure(highlightbackground="#d9d9d9")
    encryptPolybius.configure(highlightcolor="black")
    encryptPolybius.configure(pady="0")
    encryptPolybius.configure(text='''Зашифровать ->''')

    decipherPolybius = Button(rishW, command=rishD)
    decipherPolybius.place(relx=0.386, rely=0.267, height=34, width=127)
    decipherPolybius.configure(activebackground="beige")
    decipherPolybius.configure(activeforeground="#000000")
    decipherPolybius.configure(background="#e9e9e9")
    decipherPolybius.configure(compound='left')
    decipherPolybius.configure(disabledforeground="#a3a3a3")
    decipherPolybius.configure(foreground="#000000")
    decipherPolybius.configure(highlightbackground="#d9d9d9")
    decipherPolybius.configure(highlightcolor="black")
    decipherPolybius.configure(pady="0")
    decipherPolybius.configure(text='''<- Рассшифровать''')

    headGrons = Label(rishW)
    headGrons.place(relx=0.319, rely=0.022, height=51, width=224)
    headGrons.configure(anchor='w')
    headGrons.configure(background="#e6fdff")
    headGrons.configure(compound='center')
    headGrons.configure(disabledforeground="#a3a3a3")
    headGrons.configure(font="-family {Segoe UI} -size 21")
    headGrons.configure(foreground="#000000")
    headGrons.configure(text='''Решетка Кардано''')

    information = Button(rishW, command=rishI)
    information.place(relx=0.95, rely=0.038, height=24, width=27)
    information.configure(background="#ffffff")
    information.configure(borderwidth="3")
    information.configure(compound='left')
    information.configure(cursor="question_arrow")
    information.configure(font="-family {Segoe UI} -size 11")
    information.configure(foreground="#000000")
    information.configure(text='''?''')

    genKey = Button(rishW, command=genKey)
    genKey.place(relx=0.386, rely=0.511, height=34, width=127)
    genKey.configure(activebackground="beige")
    genKey.configure(activeforeground="#000000")
    genKey.configure(background="#e9e9e9")
    genKey.configure(compound='left')
    genKey.configure(disabledforeground="#a3a3a3")
    genKey.configure(foreground="#000000")
    genKey.configure(highlightbackground="#d9d9d9")
    genKey.configure(highlightcolor="black")
    genKey.configure(pady="0")
    genKey.configure(text='''Случайная решетка''')

    headChar = Label(rishW)
    headChar.place(relx=0.403, rely=0.356, height=21, width=113)
    headChar.configure(anchor='w')
    headChar.configure(background="#e6fdff")
    headChar.configure(compound='left')
    headChar.configure(disabledforeground="#a3a3a3")
    headChar.configure(foreground="#000000")
    headChar.configure(text='''Размер решетки''')

    TCombobox1 = ttk.Combobox(rishW)
    TCombobox1.place(relx=0.688, rely=0.533, relheight=0.047
                          , relwidth=0.24)
    TCombobox1['values'] = ("Без мусора", "С мусором")
    TCombobox1.current(0)

    rishW.mainloop()