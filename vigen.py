from tkinter import *
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import messagebox
from tkinter import filedialog as fd
alphabetRUS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabetENG = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfENG='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
alfRUS='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
def vigen():
    def match(text, alphabet):
        text=text.upper()
        for c in text:
            if c in alphabet:
                return True
        return False
    def keyF(key):
        for char in key:  # copies and iterates passing a value to char everytime
            key = key[1:]  # deletes the first character in the string x
            if char in key:  # checks if there is char in x string
                return False
        return True
    def f(text, key, A, op):
        #key *= len(text) // len(key) + 1
        openText1 = text  # Открытый текст
        cipherSTR = ""
        simvol = [[], []]
        openText2 = openText1.upper()
        tempSTR=openText2
        for k in range(len(openText2)):
            if not (openText2[k] in A):
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
    def vigenE():
        openSTR = openText.get(1.0, END)
        keySTR = keyGrons.get()
        keySTR = keySTR.upper()
        key = ''
        language = TCombobox1.get()
        if language == "Русский":
            if 0:
                messagebox.showerror('Ошибка', 'Неверный алфавит.')
            else:
                if not keySTR.isalpha() or match(keySTR, alphabetENG):
                    messagebox.showerror('Ошибка', 'Неверный ключ.')
                else:
                    for i in keySTR:
                        for j in range(len(alphabetRUS)):
                            if i == alphabetRUS[j]:
                                key = key + str(j) + " "
                    key = key.split()

                    cipherText.delete(1.0, END)
                    cipherText.insert(1.0, f(openSTR, key, alphabetRUS, 1))

        if language == "Английский":
            if match(openSTR,alphabetRUS):
                messagebox.showerror('Ошибка', 'Неверный алфавит.')
            else:
                if not keySTR.isalpha() or match(keySTR, alphabetRUS):
                    messagebox.showerror('Ошибка', 'Неверный ключ.')
                else:
                    for i in keySTR:
                        for j in range(len(alphabetENG)):
                            if i == alphabetENG[j]:
                                key = key + str(j) + " "
                    key = key.split()

                    cipherText.delete(1.0, END)
                    cipherText.insert(1.0, f(openSTR, key, alphabetENG, 1))

    def vigenD():
        openSTR = cipherText.get(1.0, END)
        keySTR = keyGrons.get()
        keySTR = keySTR.upper()
        key = ''
        language = TCombobox1.get()
        if language == "Русский":
            if match(openSTR,alphabetENG):
                messagebox.showerror('Ошибка', 'Неверный алфавит.')
            else:
                if not keySTR.isalpha() or match(keySTR, alphabetENG):
                    messagebox.showerror('Ошибка', 'Неверный ключ.')
                else:
                    for i in keySTR:
                        for j in range(len(alphabetRUS)):
                            if i == alphabetRUS[j]:
                                key = key + str(j) + " "
                    key = key.split()

                    openText.delete(1.0, END)
                    openText.insert(1.0, f(openSTR, key, alphabetRUS, -1))

        if language == "Английский":
            if match(openSTR,alphabetRUS):
                messagebox.showerror('Ошибка', 'Неверный алфавит.')
            else:
                if not keySTR.isalpha() or match(keySTR, alphabetRUS):
                    messagebox.showerror('Ошибка', 'Неверный ключ.')
                else:
                    for i in keySTR:
                        for j in range(len(alphabetENG)):
                            if i == alphabetENG[j]:
                                key = key + str(j) + " "
                    key = key.split()

                    openText.delete(1.0, END)
                    openText.insert(1.0, f(openSTR, key, alphabetENG, -1))
    def encrip():
        openSTR = openText.get(1.0, END)
        keySTR = keyGrons.get()
        keySTR = keySTR.upper()
        key = ''
        language = TCombobox1.get()
        if language == "Русский":
            if match(openSTR,alphabetENG):
                messagebox.showerror('Ошибка', 'Неверный алфавит.')
            else:
                if not keySTR.isalpha() or match(keySTR, alphabetENG):
                    messagebox.showerror('Ошибка', 'Неверный ключ.')
                else:
                    for i in keySTR:
                        for j in range(len(alphabetRUS)):
                            if i == alphabetRUS[j]:
                                key = key + str(j) + " "
                    key = key.split()

                    cipherText.delete(1.0, END)
                    cipherText.insert(1.0, f(openSTR, key, alphabetRUS, -1))

        if language == "Английский":
            if match(openSTR,alphabetRUS):
                messagebox.showerror('Ошибка', 'Неверный алфавит.')
            else:
                if not keySTR.isalpha() or match(keySTR, alphabetRUS):
                    messagebox.showerror('Ошибка', 'Неверный ключ.')
                else:
                    for i in keySTR:
                        for j in range(len(alphabetENG)):
                            if i == alphabetENG[j]:
                                key = key + str(j) + " "
                    key = key.split()

                    openText.delete(1.0, END)
                    openText.insert(1.0, f(openSTR, key, alphabetENG, -1))
    def vigenI():
        messagebox.showinfo('О Шифре Виженера', 'Ожидается')
    def openF():
        inFile = fd.askopenfilename()
        f = open(inFile, encoding="utf-8")
        #f = open(inFile, encoding="utf-8")
        s = f.read()
        openText.delete(1.0, END)
        openText.insert(1.0, s)
        f.close()
    def saveF():
        outFile = fd.asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),
                       ("All files", "*.*")))
        f = open(outFile, 'w', encoding="utf-8")
        s = cipherText.get(1.0, END)
        f.write(s)
        f.close()
    vigenW = Tk()
    vigenW.geometry("716x263+322+179")
    vigenW.title("Шифр Виженера")
    vigenW.configure(background="#ffcece")

    openText = Text(vigenW)
    openText.place(relx=0.029, rely=0.3, relheight=0.612, relwidth=0.37)
    openText.configure(background="white")
    openText.configure(borderwidth="2")
    openText.configure(font="-family {@Malgun Gothic} -size 13")
    openText.configure(foreground="black")

    cipherText = Text(vigenW)
    cipherText.place(relx=0.601, rely=0.3, relheight=0.612, relwidth=0.37)
    cipherText.configure(background="white")
    cipherText.configure(borderwidth="2")
    cipherText.configure(font="-family {@Malgun Gothic} -size 13")
    cipherText.configure(foreground="black")

    encryptPolybius = Button(vigenW, command=vigenE)
    encryptPolybius.place(relx=0.419, rely=0.305, height=34, width=115)
    encryptPolybius.configure(background="#ffffff")
    encryptPolybius.configure(borderwidth="3")
    encryptPolybius.configure(cursor="hand2")
    encryptPolybius.configure(font="-family {@Malgun Gothic} -size 10")
    encryptPolybius.configure(foreground="#000000")
    encryptPolybius.configure(text='''Зашифровать ->''')

    decipherPolybius = Button(vigenW, command=vigenD)
    decipherPolybius.place(relx=0.419, rely=0.455, height=34, width=114)
    decipherPolybius.configure(background="#ffffff")
    decipherPolybius.configure(borderwidth="3")
    decipherPolybius.configure(cursor="hand2")
    decipherPolybius.configure(font="-family {@Malgun Gothic} -size 10")
    decipherPolybius.configure(foreground="#000000")
    decipherPolybius.configure(text='''<-Расшифровать''')

    headGrons = Label(vigenW)
    headGrons.place(relx=0.279, rely=0.075, height=52, width=341)
    headGrons.configure(background="#ffcece")
    headGrons.configure(font="-family {Open Sans Light} -size 20 -weight bold")
    headGrons.configure(foreground="#000000")
    headGrons.configure(text='''Шифр Виженера''')

    information = Button(vigenW, command=vigenI)
    information.place(relx=0.95, rely=0.038, height=24, width=27)
    information.configure(background="#ffffff")
    information.configure(borderwidth="3")
    information.configure(compound='left')
    information.configure(cursor="question_arrow")
    information.configure(font="-family {Segoe UI} -size 11")
    information.configure(foreground="#000000")
    information.configure(text='''?''')

    headChar = Label(vigenW)
    headChar.place(relx=0.412, rely=0.865, height=21, width=134)
    headChar.configure(background="#ffcece")
    headChar.configure(disabledforeground="#a3a3a3")
    headChar.configure(font="-family {@Malgun Gothic} -size 8")
    headChar.configure(foreground="#000000")
    headChar.configure(text='''Ключ''')

    keyGrons = Entry(vigenW)
    keyGrons.place(relx=0.419, rely=0.771, height=30, relwidth=0.159)
    keyGrons.configure(background="white")
    keyGrons.configure(borderwidth="2")
    keyGrons.configure(font="-family {@Malgun Gothic} -size 14")
    keyGrons.configure(foreground="#000000")

    TCombobox1 = ttk.Combobox(vigenW)
    TCombobox1.place(relx=0.768, rely=0.038, relheight=0.079
                          , relwidth=0.158)
    TCombobox1['values'] = ("Русский", "Английский")
    TCombobox1.current(0)  # установите вариант по умолчанию
    openF = Button(vigenW, command=openF)
    openF.place(relx=0.028, rely=0.15, height=24, width=147)
    openF.configure(background="#ffffff")
    openF.configure(borderwidth="3")
    openF.configure(compound='left')
    openF.configure(cursor="hand2")
    openF.configure(font="-family {@Malgun Gothic} -size 10")
    openF.configure(text='''Открыть файл''')

    saveF = Button(vigenW, command=saveF)
    saveF.place(relx=0.768, rely=0.15, height=24, width=147)
    saveF.configure(background="#ffffff")
    saveF.configure(borderwidth="3")
    saveF.configure(compound='left')
    saveF.configure(cursor="hand2")
    saveF.configure(font="-family {@Malgun Gothic} -size 10")
    saveF.configure(text='''Сохранить в файл''')

    keyButton = Button(vigenW, command=encrip)
    keyButton.place(relx=0.419, rely=0.605, height=34, width=113)
    keyButton.configure(background="#ffffff")
    keyButton.configure(borderwidth="3")
    keyButton.configure(cursor="hand2")
    keyButton.configure(font="-family {@Malgun Gothic} -size 10")
    keyButton.configure(foreground="#000000")
    keyButton.configure(text='''Расшифровать ->''')
    vigenW.mainloop()