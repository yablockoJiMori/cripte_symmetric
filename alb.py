from tkinter import *
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import messagebox
alphabetRUS=set('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя')
alphabetENG=set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
def match(text,alphabet):
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
def alb():

    def albE():
        openSTR = openText.get(1.0, END)
        key = keyPolybius.get()
        shift = charPolybius.get()
        language = TCombobox1.get()
        if language == "Русский":
                if  match(openSTR,alphabetENG):
                    messagebox.showerror('Ошибка', 'Неверный алфавит.')
                else:
                    if not key.isalpha() or match(key,alphabetENG) or not keyF(key):
                        messagebox.showerror('Ошибка', 'Неверный ключ.')
                    else:
                        if not shift.isdigit():
                            messagebox.showerror('Ошибка', 'Неверный сдвиг.')
                        else:
                            rusB = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"  # Алфавит
                            key = key.upper() # Кодовое слово
                            rusBtemp = rusB
                            for i in range(len(key)):
                                rusBtemp = rusBtemp.replace(key[i], '')
                            rusA = key + rusBtemp

                            openText1 = openSTR  # Открытый текст
                            cipherSTR = ""
                            simvol = [[], []]
                            openText2 = openText1.upper()
                            tempSTR = openText2
                            for k in range(len(openText2)):
                                if not openText2[k].isalpha():
                                    simvol[0].append(openText2[k])
                                    simvol[1].append(k)
                                    tempSTR = tempSTR.replace(openText2[k], "")
                            openText2 = tempSTR
                            n = int(shift)
                            n = n % len(rusB)
                            for i in range(len(openText2)):
                                for j in range(len(rusB)):
                                    if rusB[j]==openText2[i]:
                                        cipherSTR+=rusA[j]
                                rusA = rusA[n:] + rusA[:n]
                            for i in range(len(simvol[0])-1):
                                cipherSTR = cipherSTR[:int(simvol[1][i])] + simvol[0][i] + cipherSTR[int(simvol[1][i]):]
                            for i in range(len(cipherSTR)):
                                  if openText1[i].islower():
                                      cipherSTR = cipherSTR[:i] + cipherSTR[i].lower() + cipherSTR[i + 1:]
                                # Вывод криптограммы
                            cipherText.delete(1.0, END)
                            cipherText.insert(1.0, cipherSTR)
        if language == "Английский":
            if match(openSTR, alphabetRUS):
                messagebox.showerror('Ошибка', 'Неверный алфавит.')
            else:
                if not key.isalpha() or match(key, alphabetRUS) or not keyF(key):
                    messagebox.showerror('Ошибка', 'Неверный ключ.')
                else:
                    if not shift.isdigit():
                        messagebox.showerror('Ошибка', 'Неверный сдвиг.')
                    else:
                        engB = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Алфавит
                         # Кодовое слово
                        key = key.upper()
                        engBtemp = engB
                        for i in range(len(key)):
                            engBtemp = engBtemp.replace(key[i], '')
                        engA = key + engBtemp

                        # Зашифрование
                        openText1 = openSTR  # Открытый текст
                        cipherSTR = ""
                        simvol = [[], []]
                        openText2 = openText1.upper()
                        tempSTR = openText2
                        for k in range(len(openText2)):
                            if not openText2[k].isalpha():
                                simvol[0].append(openText2[k])
                                simvol[1].append(k)
                                tempSTR = tempSTR.replace(openText2[k], "")
                        openText2 = tempSTR
                        n = int(shift)
                        n = n % len(engB)
                        for i in range(len(openText2)):
                            for j in range(len(engB)):
                                if engB[j] == openText2[i]:
                                    cipherSTR += engA[j]
                            engA = engA[n:] + engA[:n]
                        for i in range(len(simvol[0]) - 1):
                            cipherSTR = cipherSTR[:int(simvol[1][i])] + simvol[0][i] + cipherSTR[int(simvol[1][i]):]
                        for i in range(len(cipherSTR)):
                            if openText1[i].islower():
                                cipherSTR = cipherSTR[:i] + cipherSTR[i].lower() + cipherSTR[i + 1:]
                        # Вывод криптограммы
                        cipherText.delete(1.0, END)
                        cipherText.insert(1.0, cipherSTR)


    def albD():
        cipherSTR = cipherText.get(1.0, END)
        key = keyPolybius.get()
        shift = charPolybius.get()
        language = TCombobox1.get()
        if language == "Русский":
            if match(cipherSTR, alphabetENG):
                messagebox.showerror('Ошибка', 'Неверный алфавит.')
            else:
                if not key.isalpha() or match(key, alphabetENG) or not keyF(key):
                    messagebox.showerror('Ошибка', 'Неверный ключ.')
                else:
                    if not shift.isdigit():
                        messagebox.showerror('Ошибка', 'Неверный сдвиг.')
                    else:
                        rusB = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"  # Алфавит
                        key = key.upper()  # Кодовое слово
                        rusBtemp = rusB
                        for i in range(len(key)):
                            rusBtemp = rusBtemp.replace(key[i], '')
                        rusA= key + rusBtemp

                        openText2 = ""
                        simvol = [[], []]
                        cipherText1 = cipherSTR
                        cipherSTR = cipherText1.upper()
                        tempSTR = cipherSTR
                        for k in range(len(cipherSTR)):
                            if not cipherSTR[k].isalpha():
                                simvol[0].append(cipherSTR[k])
                                simvol[1].append(k)
                                tempSTR = tempSTR.replace(cipherSTR[k], "")
                        cipherSTR = tempSTR
                        n = int(shift)
                        n = n % len(rusB)
                        for i in range(len(cipherSTR)-1):
                            rusA = rusA[n:] + rusA[:n]
                        cipherSTR=cipherSTR[::-1]
                        for i in range(len(cipherSTR)):
                            for j in range(len(rusA)):
                                if rusA[j] == cipherSTR[i]:
                                    openText2 += rusB[j]
                            rusA = rusA[(-n):] + rusA[:(-n)]
                        openText2 = openText2[::-1]

                        for i in range(len(simvol[0])-1):
                            openText2 = openText2[:int(simvol[1][i])] + simvol[0][i] + openText2[int(simvol[1][i]):]

                        for i in range(len(openText2)):
                            if cipherText1[i].islower():
                                openText2 = openText2[:i] + openText2[i].lower() + openText2[i + 1:]
                         # Вывод расшифрованного
                        openText.delete(1.0, END)
                        openText.insert(1.0, openText2)
        if language == "Английский":
            if match(cipherSTR, alphabetRUS):
                messagebox.showerror('Ошибка', 'Неверный алфавит.')
            else:
                if not key.isalpha() or match(key, alphabetRUS) or not keyF(key):
                    messagebox.showerror('Ошибка', 'Неверный ключ.')
                else:
                    if not shift.isdigit():
                        messagebox.showerror('Ошибка', 'Неверный сдвиг.')
                    else:
                        engB = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Алфавит
                         # Кодовое слово
                        key = key.upper()  # Кодовое слово
                        engBtemp = engB
                        for i in range(len(key)):
                            engBtemp = engBtemp.replace(key[i], '')
                        engA = key + engBtemp

                        openText2 = ""
                        simvol = [[], []]
                        cipherText1 = cipherSTR
                        cipherSTR = cipherText1.upper()
                        tempSTR = cipherSTR
                        for k in range(len(cipherSTR)):
                            if not cipherSTR[k].isalpha():
                                simvol[0].append(cipherSTR[k])
                                simvol[1].append(k)
                                tempSTR = tempSTR.replace(cipherSTR[k], "")
                        cipherSTR = tempSTR
                        n = int(shift)
                        n = n % len(engB)
                        for i in range(len(cipherSTR) - 1):
                            engA = engA[n:] + engA[:n]
                        cipherSTR = cipherSTR[::-1]
                        for i in range(len(cipherSTR)):
                            for j in range(len(engA)):
                                if engA[j] == cipherSTR[i]:
                                    openText2 += engB[j]
                            engA = engA[(-n):] + engA[:(-n)]
                        openText2 = openText2[::-1]

                        for i in range(len(simvol[0]) - 1):
                            openText2 = openText2[:int(simvol[1][i])] + simvol[0][i] + openText2[int(simvol[1][i]):]

                        for i in range(len(openText2)):
                            if cipherText1[i].islower():
                                openText2 = openText2[:i] + openText2[i].lower() + openText2[i + 1:]
                        # Вывод расшифрованного
                        openText.delete(1.0, END)
                        openText.insert(1.0, openText2)


    def albI():
        messagebox.showinfo('О Шифре Альберти', 'Ожидается')

    albW = Tk()
    albW.geometry("716x263+322+179")
    albW.title("Шифр Альберти")
    albW.configure(background="#ffcece")

    openText = Text(albW)
    openText.place(relx=0.029, rely=0.3, relheight=0.612, relwidth=0.37)
    openText.configure(background="white")
    openText.configure(borderwidth="2")
    openText.configure(font="-family {@Malgun Gothic} -size 13")
    openText.configure(foreground="black")

    cipherText = Text(albW)
    cipherText.place(relx=0.601, rely=0.3, relheight=0.612, relwidth=0.37)
    cipherText.configure(background="white")
    cipherText.configure(borderwidth="2")
    cipherText.configure(font="-family {@Malgun Gothic} -size 13")
    cipherText.configure(foreground="black")

    encryptPolybius = Button(albW, command=albE)
    encryptPolybius.place(relx=0.419, rely=0.305, height=34, width=115)
    encryptPolybius.configure(background="#ffffff")
    encryptPolybius.configure(borderwidth="3")
    encryptPolybius.configure(cursor="hand2")
    encryptPolybius.configure(font="-family {@Malgun Gothic} -size 10")
    encryptPolybius.configure(foreground="#000000")
    encryptPolybius.configure(text='''Зашифровать ->''')

    decipherPolybius = Button(albW, command=albD)
    decipherPolybius.place(relx=0.419, rely=0.455, height=34, width=114)
    decipherPolybius.configure(background="#ffffff")
    decipherPolybius.configure(borderwidth="3")
    decipherPolybius.configure(cursor="hand2")
    decipherPolybius.configure(font="-family {@Malgun Gothic} -size 10")
    decipherPolybius.configure(foreground="#000000")
    decipherPolybius.configure(text='''<-Расшифровать''')

    headPolybius = Label(albW)
    headPolybius.place(relx=0.279, rely=0.075, height=52, width=341)
    headPolybius.configure(background="#ffcece")
    headPolybius.configure(font="-family {Open Sans Light} -size 20 -weight bold")
    headPolybius.configure(foreground="#000000")
    headPolybius.configure(text='''Шифр Альберти''')

    information = Button(albW, command=albI)
    information.place(relx=0.95, rely=0.038, height=24, width=27)
    information.configure(background="#ffffff")
    information.configure(borderwidth="3")
    information.configure(compound='left')
    information.configure(cursor="question_arrow")
    information.configure(font="-family {Segoe UI} -size 11")
    information.configure(foreground="#000000")
    information.configure(text='''?''')

    keyPolybius = Entry(albW)
    keyPolybius.place(relx=0.419, rely=0.602, height=30, relwidth=0.159)
    keyPolybius.configure(background="white")
    keyPolybius.configure(borderwidth="2")
    keyPolybius.configure(font="-family {@Malgun Gothic} -size 14")
    keyPolybius.configure(foreground="#000000")

    headKey = Label(albW)
    headKey.place(relx=0.425, rely=0.714, height=11, width=103)
    headKey.configure(background="#ffcece")
    headKey.configure(font="-family {@Malgun Gothic} -size 8")
    headKey.configure(foreground="#000000")
    headKey.configure(text='''Ключевое слово''')

    headChar = Label(albW)
    headChar.place(relx=0.412, rely=0.865, height=21, width=134)
    headChar.configure(background="#ffcece")
    headChar.configure(disabledforeground="#a3a3a3")
    headChar.configure(font="-family {@Malgun Gothic} -size 8")
    headChar.configure(foreground="#000000")
    headChar.configure(text='''Сдвиг''')

    charPolybius = Entry(albW)
    charPolybius.place(relx=0.419, rely=0.771, height=30, relwidth=0.159)
    charPolybius.configure(background="white")
    charPolybius.configure(borderwidth="2")
    charPolybius.configure(font="-family {@Malgun Gothic} -size 14")
    charPolybius.configure(foreground="#000000")

    TCombobox1 = ttk.Combobox(albW)
    TCombobox1.place(relx=0.768, rely=0.038, relheight=0.079
                          , relwidth=0.158)
    TCombobox1['values'] = ("Русский", "Английский")
    TCombobox1.current(0)  # установите вариант по умолчанию

    albW.mainloop()