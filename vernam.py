from tkinter import *
from tkinter.constants import *
from tkinter import messagebox
import numpy as np
def vernam():
    def encode(s):
        return list(map(lambda x: "{0:b}".format(ord(x)).zfill(16), s))

    def decode(lst):
        return ''.join(map(lambda x: chr(int(x, 2)), lst))
    def keyCr():
        openSTR = openText.get(1.0, END)
        openSTR=openSTR[:-1]

        keyBin = [[0] * 16 for i in range(len(openSTR))]

        for i in range(len(openSTR)):
            for j in range(16):
                keyBin[i][j] = np.random.randint(0, 2)
        for i in range(len(openSTR)):
            keyBin[i] = "".join(map(str, keyBin[i]))
        key = decode(keyBin)
        keyGrons.delete(0, END)
        keyGrons.insert(0, key)


    def rishE():
        openSTR = openText.get(1.0, END)
        openSTR=openSTR[:-1]
        key = keyGrons.get()
        if len(key) != len(openSTR):
            messagebox.showerror('Ошибка', 'Неверный ключ.')
        else:

            openSTRbin = encode(openSTR)
            keyBin = encode(key)
            cipherSTRbin = [[0] * 16 for i in range(len(openSTRbin))]
            for i in range(len(openSTRbin)):
                for j in range(16):
                    cipherSTRbin[i][j] = int(openSTRbin[i][j]) ^ int(keyBin[i][j])
            for i in range(len(openSTRbin)):
                cipherSTRbin[i] = "".join(map(str, cipherSTRbin[i]))
            cipherSTR = decode(cipherSTRbin)
            if not cipherSTR.isprintable() :
                messagebox.showerror('Ошибка', 'Ошибка зашифрования, введите другой ключ.')
            else:
                cipherText.delete(1.0, END)
                cipherText.insert(1.0, cipherSTR)


    def rishD():
        openSTR = cipherText.get(1.0, END)
        openSTR = openSTR[:-1]
        key = keyGrons.get()
        if len(key) != len(openSTR):
            messagebox.showerror('Ошибка', 'Неверный ключ.')
        else:

            openSTRbin = encode(openSTR)
            keyBin = encode(key)
            cipherSTRbin = [[0] * 16 for i in range(len(openSTRbin))]
            for i in range(len(openSTRbin)):
                for j in range(16):
                    cipherSTRbin[i][j] = int(openSTRbin[i][j]) ^ int(keyBin[i][j])
            for i in range(len(openSTRbin)):
                cipherSTRbin[i] = "".join(map(str, cipherSTRbin[i]))
            cipherSTR = decode(cipherSTRbin)
            openText.delete(1.0, END)
            openText.insert(1.0, cipherSTR)


    def rishI():
        messagebox.showinfo('О Шифре Ришелье', 'Ожидается')

    rishW = Tk()
    rishW.geometry("716x263+322+179")
    rishW.title("Шифр Вернама")
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
    headGrons.configure(text='''Шифр Вернама''')

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