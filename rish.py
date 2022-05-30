from tkinter import *
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import messagebox
import re
def rish():
    def rishE():
        openSTR = openText.get(1.0, END)
        key = keyGrons.get()
        if not re.match(r"^\(\d+(,\d+|\)\(\d+)*\)$", key):
            messagebox.showerror('Ошибка', 'Неверный ключ1.')
        else:
            key = key.replace("(", "", 1)
            key = key.replace(")", "")
            key = key.split("(")
            for i in range(len(key)):
                key[i] = key[i].split(",")
            sum = 0
            for i in range(len(key)):
                for j in range(len(key[i])):
                    key[i][j] = int(key[i][j])
                    sum += 1
            if sum != (len(openSTR)-1):
                messagebox.showerror('Ошибка', 'Неверный ключ2.')
            else:
                flacSTR = []
                for i in range(len(key)):
                    for k in range(len(key[i])):
                        flac = 0
                        for j in range(len(key[i])):
                            if (k + 1) == key[i][j]:
                                flac += 1
                        flacSTR.append(flac)
                if flacSTR != [1] * (len(openSTR)-1):
                    messagebox.showerror('Ошибка', 'Неверный ключ3.')
                else:
                    cipherSTR = ""
                    point = -1
                    for i in range(len(key)):
                        segment = ""
                        for j in range(len(key[i])):
                            segment += openSTR[point + key[i][j]]
                        cipherSTR += segment
                        point += len(key[i])

                    cipherText.delete(1.0, END)
                    cipherText.insert(1.0, cipherSTR)

    def rishD():
        openSTR = cipherText.get(1.0, END)
        key = keyGrons.get()
        if not re.match(r"^\(\d+(,\d+|\)\(\d+)*\)$", key):
            messagebox.showerror('Ошибка', 'Неверный ключ1.')
        else:
            key = key.replace("(", "", 1)
            key = key.replace(")", "")
            key = key.split("(")
            for i in range(len(key)):
                key[i] = key[i].split(",")
            sum = 0
            for i in range(len(key)):
                for j in range(len(key[i])):
                    key[i][j] = int(key[i][j])
                    sum += 1
            # array = []
            # for subkey in key:
            #     subkey = tuple(map(int, subkey.split(" ")))
            #     array.append(subkey)
            if sum != (len(openSTR) - 1):
                messagebox.showerror('Ошибка', 'Неверный ключ2.')
            else:
                flacSTR = []
                for i in range(len(key)):
                    for k in range(len(key[i])):
                        flac = 0
                        for j in range(len(key[i])):
                            if (k + 1) == key[i][j]:
                                flac += 1
                        flacSTR.append(flac)
                if flacSTR != [1] * (len(openSTR) - 1):
                    messagebox.showerror('Ошибка', 'Неверный ключ3.')
                else:
                    cipherSTRarr = [None] * (len(openSTR)-1)
                    point = -1
                    flag = 0
                    for i in range(len(key)):
                        for j in range(len(key[i])):
                            cipherSTRarr[key[i][j] + point] = openSTR[flag]
                            flag += 1
                        point += len(key[i])
                        cipherSTR = ""
                        for i in range(len(cipherSTRarr)):
                            cipherSTR += str(cipherSTRarr[i])

                    openText.delete(1.0, END)
                    openText.insert(1.0, cipherSTR)


    def rishI():
        messagebox.showinfo('О Шифре Ришелье', 'Ожидается')

    rishW = Tk()
    rishW.geometry("716x263+322+179")
    rishW.title("Шифр Ришелье")
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

    encryptPolybius = Button(rishW, command=rishE)
    encryptPolybius.place(relx=0.419, rely=0.305, height=34, width=115)
    encryptPolybius.configure(background="#ffffff")
    encryptPolybius.configure(borderwidth="3")
    encryptPolybius.configure(cursor="hand2")
    encryptPolybius.configure(font="-family {@Malgun Gothic} -size 10")
    encryptPolybius.configure(foreground="#000000")
    encryptPolybius.configure(text='''Зашифровать ->''')

    decipherPolybius = Button(rishW, command=rishD)
    decipherPolybius.place(relx=0.419, rely=0.455, height=34, width=114)
    decipherPolybius.configure(background="#ffffff")
    decipherPolybius.configure(borderwidth="3")
    decipherPolybius.configure(cursor="hand2")
    decipherPolybius.configure(font="-family {@Malgun Gothic} -size 10")
    decipherPolybius.configure(foreground="#000000")
    decipherPolybius.configure(text='''<-Расшифровать''')

    headGrons = Label(rishW)
    headGrons.place(relx=0.279, rely=0.075, height=52, width=341)
    headGrons.configure(background="#ffcece")
    headGrons.configure(font="-family {Open Sans Light} -size 20 -weight bold")
    headGrons.configure(foreground="#000000")
    headGrons.configure(text='''Шифр Ришелье''')

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