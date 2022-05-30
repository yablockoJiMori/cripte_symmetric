from tkinter import *
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import messagebox
alphabetRUS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabetENG = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def grons():
    def match(text, alphabet):
        text=text.upper()
        for c in text:
            if c in alphabet:
                return True
        return False
    def f(text, key, A, op):
        #key *= len(text) // len(key) + 1
        openText1 = text  # Открытый текст
        cipherSTR = ""
        simvol = [[], []]
        openText2 = openText1.upper()
        tempSTR=openText2
        for k in range(len(openText2)):
            if not openText2[k].isalpha():
                simvol[0].append(openText2[k])
                simvol[1].append(k)
                tempSTR=tempSTR.replace(openText2[k],"")
        openText2=tempSTR
        cipherSTR=cipherSTR.join([A[(A.index(j) + int(key[i%len(key)]) * op) % len(A)] for i, j in enumerate(openText2)])
        for i in range(len(simvol[0])-1):
            cipherSTR = cipherSTR[:int(simvol[1][i])] + simvol[0][i] + cipherSTR[int(simvol[1][i]):]
        for i in range(len(cipherSTR)):
            if openText1[i].islower():
                cipherSTR = cipherSTR[:i] + cipherSTR[i].lower() + cipherSTR[i + 1:]
        return cipherSTR
    def gronsE():
        openSTR = openText.get(1.0, END)
        key = keyGrons.get()
        language = TCombobox1.get()
        if language == "Русский":
            if match(openSTR,alphabetENG):
                messagebox.showerror('Ошибка', 'Неверный алфавит.')
            else:
                if not key.isdigit():
                    messagebox.showerror('Ошибка', 'Неверный ключ.')
                else:
                    cipherText.delete(1.0, END)
                    cipherText.insert(1.0, f(openSTR, key, alphabetRUS, 1))

        if language == "Английский":
            if match(openSTR,alphabetRUS):
                messagebox.showerror('Ошибка', 'Неверный алфавит.')
            else:
                if not key.isdigit():
                    messagebox.showerror('Ошибка', 'Неверный ключ.')
                else:
                    cipherText.delete(1.0, END)
                    cipherText.insert(1.0, f(openSTR, key, alphabetENG, 1))

    def gronsD():
        openSTR = cipherText.get(1.0, END)
        key = keyGrons.get()
        language = TCombobox1.get()
        if language == "Русский":
            if match(openSTR,alphabetENG):
                messagebox.showerror('Ошибка', 'Неверный алфавит.')
            else:
                if not key.isdigit():
                    messagebox.showerror('Ошибка', 'Неверный ключ.')
                else:
                    openText.delete(1.0, END)
                    openText.insert(1.0, f(openSTR, key, alphabetRUS, -1))

        if language == "Английский":
            if match(openSTR,alphabetRUS):
                messagebox.showerror('Ошибка', 'Неверный алфавит.')
            else:
                if not key.isdigit():
                    messagebox.showerror('Ошибка', 'Неверный ключ.')
                else:
                    openText.delete(1.0, END)
                    openText.insert(1.0, f(openSTR, key, alphabetENG, -1))

    def gronsI():
        messagebox.showinfo('О Шифре Гронсфельда', 'Ожидается')

    gronsW = Tk()
    gronsW.geometry("716x263+322+179")
    gronsW.title("Шифр Гронсфельда")
    gronsW.configure(background="#ffcece")

    openText = Text(gronsW)
    openText.place(relx=0.029, rely=0.3, relheight=0.612, relwidth=0.37)
    openText.configure(background="white")
    openText.configure(borderwidth="2")
    openText.configure(font="-family {@Malgun Gothic} -size 13")
    openText.configure(foreground="black")

    cipherText = Text(gronsW)
    cipherText.place(relx=0.601, rely=0.3, relheight=0.612, relwidth=0.37)
    cipherText.configure(background="white")
    cipherText.configure(borderwidth="2")
    cipherText.configure(font="-family {@Malgun Gothic} -size 13")
    cipherText.configure(foreground="black")

    encryptPolybius = Button(gronsW, command=gronsE)
    encryptPolybius.place(relx=0.419, rely=0.305, height=34, width=115)
    encryptPolybius.configure(background="#ffffff")
    encryptPolybius.configure(borderwidth="3")
    encryptPolybius.configure(cursor="hand2")
    encryptPolybius.configure(font="-family {@Malgun Gothic} -size 10")
    encryptPolybius.configure(foreground="#000000")
    encryptPolybius.configure(text='''Зашифровать ->''')

    decipherPolybius = Button(gronsW, command=gronsD)
    decipherPolybius.place(relx=0.419, rely=0.455, height=34, width=114)
    decipherPolybius.configure(background="#ffffff")
    decipherPolybius.configure(borderwidth="3")
    decipherPolybius.configure(cursor="hand2")
    decipherPolybius.configure(font="-family {@Malgun Gothic} -size 10")
    decipherPolybius.configure(foreground="#000000")
    decipherPolybius.configure(text='''<-Расшифровать''')

    headGrons = Label(gronsW)
    headGrons.place(relx=0.279, rely=0.075, height=52, width=341)
    headGrons.configure(background="#ffcece")
    headGrons.configure(font="-family {Open Sans Light} -size 20 -weight bold")
    headGrons.configure(foreground="#000000")
    headGrons.configure(text='''Шифр Гронсфельда''')

    information = Button(gronsW, command=gronsI)
    information.place(relx=0.95, rely=0.038, height=24, width=27)
    information.configure(background="#ffffff")
    information.configure(borderwidth="3")
    information.configure(compound='left')
    information.configure(cursor="question_arrow")
    information.configure(font="-family {Segoe UI} -size 11")
    information.configure(foreground="#000000")
    information.configure(text='''?''')

    headChar = Label(gronsW)
    headChar.place(relx=0.412, rely=0.865, height=21, width=134)
    headChar.configure(background="#ffcece")
    headChar.configure(disabledforeground="#a3a3a3")
    headChar.configure(font="-family {@Malgun Gothic} -size 8")
    headChar.configure(foreground="#000000")
    headChar.configure(text='''Ключ''')

    keyGrons = Entry(gronsW)
    keyGrons.place(relx=0.419, rely=0.771, height=30, relwidth=0.159)
    keyGrons.configure(background="white")
    keyGrons.configure(borderwidth="2")
    keyGrons.configure(font="-family {@Malgun Gothic} -size 14")
    keyGrons.configure(foreground="#000000")

    TCombobox1 = ttk.Combobox(gronsW)
    TCombobox1.place(relx=0.768, rely=0.038, relheight=0.079
                          , relwidth=0.158)
    TCombobox1['values'] = ("Русский", "Английский")
    TCombobox1.current(0)  # установите вариант по умолчанию

    gronsW.mainloop()