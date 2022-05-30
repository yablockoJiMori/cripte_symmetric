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
def playfair():

    def polybiusE():
        openSTR = openText.get(1.0, END)
        openSTR = openSTR[:-1]
        key = keyPolybius.get()
        language = TCombobox1.get()
        if language == "Русский":
                if  match(openSTR,alphabetENG):
                    messagebox.showerror('Ошибка', 'Неверный алфавит.')
                else:
                    if not key.isalpha() or match(key,alphabetENG) or not keyF(key):
                        messagebox.showerror('Ошибка', 'Неверный ключ.')
                    else:
                        if not 1:
                            messagebox.showerror('Ошибка', 'Неверный сдвиг.')
                        else:
                            rusB = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯÈÉÊ"  # Алфавит
                            key = key.upper()  # Кодовое слово
                            rusBtemp = rusB
                            for i in range(len(key)):
                                rusBtemp = rusBtemp.replace(key[i], '')
                            sq = key + rusBtemp
                            sqP = [[0 for i in range(6)] for j in range(6)]
                            for i in range(6):
                                for j in range(6):
                                    sqP[i][j] = sq[6 * i + j]
                            print(sqP)
                            openText1 = openSTR  # Открытый текст
                            cipherSTR = ""
                            simvol = [[], []]
                            slow = []

                            for k in range(len(openText1)):
                                if not openText1[k].isalpha():
                                    simvol[0].append(openText1[k])
                                    simvol[1].append(k)

                            for k in openText1:
                                if not k.isalpha():
                                    openText1 = openText1.replace(k, '')
                            for k in range(len(openText1)):
                                if openText1[k].islower():
                                    slow.append(k)
                            openText2 = openText1.upper()

                            for i in range(0, len(openText2), 2):
                                if i == len(openText2) - 1:
                                    break
                                if openText2[i] == openText2[i + 1]:
                                    if openText2[i] == "Х":
                                        openText2 = openText2[:i + 1] + "Ф" + openText2[i + 1:]
                                    else:
                                        openText2 = openText2[:i + 1] + "Х" + openText2[i + 1:]

                                    for u in range(len(simvol[1])):
                                        if i + 1 < simvol[1][u]:
                                            simvol[1][u] += 1

                                    for u in range(len(slow)):
                                        if i + 1 <= slow[u]:
                                            slow[u] += 1

                            if len(openText2) % 2 != 0:
                                openText2 = openText2 + "Х"
                            print(openText2)
                            for k in range(0, len(openText2)-1, 2):
                                l = [0, 0, 0, 0]
                                for i in range(6):
                                    for j in range(6):
                                        if openText2[k] == sqP[i][j]:
                                            l[0] = i
                                            l[1] = j
                                        if openText2[k + 1] == sqP[i][j]:
                                            l[2] = i
                                            l[3] = j
                                if l[1] == l[3]:
                                    cipherSTR = cipherSTR + sqP[(l[0] + 1) % 6][l[1]] + sqP[(l[2] + 1) % 6][l[3]]
                                    print(cipherSTR)
                                elif l[0] == l[2]:
                                    cipherSTR = cipherSTR + sqP[l[0]][(l[1] + 1) % 6] + sqP[l[2]][(l[3] + 1) % 6]
                                    print(cipherSTR)
                                else:
                                    cipherSTR = cipherSTR + sqP[l[0]][l[3]] + sqP[l[2]][l[1]]
                                    print(cipherSTR)

                            for i in slow:
                                cipherSTR = cipherSTR[:i] + cipherSTR[i].lower() + cipherSTR[i + 1:]
                            print(cipherSTR)
                            for i in range(len(simvol[0])):
                                cipherSTR = cipherSTR[:int(simvol[1][i])] + simvol[0][i] + cipherSTR[int(simvol[1][i]):]

                            cipherText.delete(1.0, END)
                            cipherText.insert(1.0, cipherSTR)
        if language == "Английский":
            if match(openSTR, alphabetRUS):
                messagebox.showerror('Ошибка', 'Неверный алфавит.')
            else:
                if not key.isalpha() or match(key, alphabetRUS) or not keyF(key):
                    messagebox.showerror('Ошибка', 'Неверный ключ.')
                else:
                    if not 1:
                        messagebox.showerror('Ошибка', 'Неверный сдвиг.')
                    else:
                        engB = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Алфавит
                        # Кодовое слово
                        key = key.upper()
                        engBtemp = engB
                        for i in range(len(key)):
                            engBtemp = engBtemp.replace(key[i], '')
                        sq = key + engBtemp
                        sqP = [[0 for i in range(5)] for j in range(5)]
                        for i in range(5):
                            for j in range(5):
                                sqP[i][j] = sq[5 * i + j]

                        # Зашифрование
                        openText1 = openSTR  # Открытый текст
                        cipherSTR = ""
                        iStr = ""
                        jStr = ""
                        simvol = [[], []]
                        slow = []

                        for k in range(len(openText1)):
                            if not openText1[k].isalpha():
                                simvol[0].append(openText1[k])
                                simvol[1].append(k)

                        for k in openText1:
                            if not k.isalpha():
                                openText1 = openText1.replace(k, '')
                        for k in range(len(openText1)):
                            if openText1[k].islower():
                                slow.append(k)
                        openText2 = openText1.upper()
                        openText2 = openText2.replace('J', 'I')

                        for i in range(0, len(openText2), 2):
                            if i == len(openText2) - 1:
                                break
                            if openText2[i] == openText2[i + 1]:
                                if openText2[i] == "X":
                                    openText2 = openText2[:i + 1] + "Q" + openText2[i + 1:]
                                else:
                                    openText2 = openText2[:i + 1] + "X" + openText2[i + 1:]

                                for u in range(len(simvol[1])):
                                    if i + 1 < simvol[1][u]:
                                        simvol[1][u] += 1

                                for u in range(len(slow)):
                                    if i + 1 <= slow[u]:
                                        slow[u] += 1

                        if len(openText2) % 2 != 0:
                            openText2 = openText2 + "X"

                        for k in range(0, len(openText2), 2):
                            l = [0, 0, 0, 0]
                            for i in range(5):
                                for j in range(5):
                                    if openText2[k] == sqP[i][j]:
                                        l[0] = i
                                        l[1] = j
                                    if openText2[k + 1] == sqP[i][j]:
                                        l[2] = i
                                        l[3] = j
                            if l[1] == l[3]:
                                cipherSTR = cipherSTR + sqP[(l[0] + 1) % 5][l[1]] + sqP[(l[2] + 1) % 5][l[3]]
                            if l[0] == l[2]:
                                cipherSTR = cipherSTR + sqP[l[0]][(l[1] + 1) % 5] + sqP[l[2]][(l[3] + 1) % 5]
                            else:
                                cipherSTR = cipherSTR + sqP[l[0]][l[3]] + sqP[l[2]][l[1]]

                        for i in slow:
                            cipherSTR = cipherSTR[:i] + cipherSTR[i].lower() + cipherSTR[i + 1:]
                        for i in range(len(simvol[0])):
                            cipherSTR = cipherSTR[:int(simvol[1][i])] + simvol[0][i] + cipherSTR[int(simvol[1][i]):]


                        cipherText.delete(1.0, END)
                        cipherText.insert(1.0, cipherSTR)


    def polybiusD():
        cipherT = cipherText.get(1.0, END)
        cipherT = cipherT[:-1]
        key = keyPolybius.get()
        language = TCombobox1.get()
        if language == "Русский":
            if match(cipherT, alphabetENG):
                messagebox.showerror('Ошибка', 'Неверный алфавит.')
            else:
                if not key.isalpha() or match(key, alphabetENG) or not keyF(key):
                    messagebox.showerror('Ошибка', 'Неверный ключ.')
                else:
                    if not 1:
                        messagebox.showerror('Ошибка', 'Неверный сдвиг.')
                    else:
                        rusB = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯÈÉÊ"  # Алфавит
                        key = key.upper()  # Кодовое слово
                        rusBtemp = rusB
                        for i in range(len(key)):
                            rusBtemp = rusBtemp.replace(key[i], '')
                        sq = key + rusBtemp
                        sqP = [[0 for i in range(6)] for j in range(6)]
                        for i in range(6):
                            for j in range(6):
                                sqP[i][j] = sq[6 * i + j]

                        openText1 = cipherT  # Открытый текст
                        cipherSTR = ""
                        simvol = [[], []]
                        slow = []

                        for k in range(len(openText1)):
                            if not openText1[k].isalpha():
                                simvol[0].append(openText1[k])
                                simvol[1].append(k)

                        for k in openText1:
                            if not k.isalpha():
                                openText1 = openText1.replace(k, '')
                        for k in range(len(openText1)):
                            if openText1[k].islower():
                                slow.append(k)
                        openText2 = openText1.upper()

                        for k in range(0, len(openText2)-1, 2):
                            l = [0, 0, 0, 0]
                            for i in range(6):
                                for j in range(6):
                                    if openText2[k] == sqP[i][j]:
                                        l[0] = i
                                        l[1] = j
                                    if openText2[k + 1] == sqP[i][j]:
                                        l[2] = i
                                        l[3] = j
                            if l[1] == l[3]:
                                cipherSTR = cipherSTR + sqP[(l[0] - 1) % 6][l[1]] + sqP[(l[2] - 1) % 6][l[3]]
                            elif l[0] == l[2]:
                                cipherSTR = cipherSTR + sqP[l[0]][(l[1] - 1) % 6] + sqP[l[2]][(l[3] - 1) % 6]
                            else:
                                cipherSTR = cipherSTR + sqP[l[0]][l[3]] + sqP[l[2]][l[1]]

                        for i in slow:
                            cipherSTR = cipherSTR[:i] + cipherSTR[i].lower() + cipherSTR[i + 1:]
                        for i in range(len(simvol[0])):
                            cipherSTR = cipherSTR[:int(simvol[1][i])] + simvol[0][i] + cipherSTR[int(simvol[1][i]):]

                        print(cipherSTR)
                        cipherSTR = cipherSTR.replace("Х", '')
                        print(cipherSTR)
                        openText.delete(1.0, END)
                        openText.insert(1.0, cipherSTR)
        if language == "Английский":
            if match(cipherT, alphabetRUS):
                messagebox.showerror('Ошибка', 'Неверный алфавит.')
            else:
                if not key.isalpha() or match(key, alphabetRUS) or not keyF(key):
                    messagebox.showerror('Ошибка', 'Неверный ключ.')
                else:
                    if not 1:
                        messagebox.showerror('Ошибка', 'Неверный сдвиг.')
                    else:
                        engB = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Алфавит
                         # Кодовое слово
                        key = key.upper()
                        engBtemp = engB
                        for i in range(len(key)):
                            engBtemp = engBtemp.replace(key[i], '')
                        sq = key + engBtemp
                        sqP = [[0 for i in range(5)] for j in range(5)]
                        for i in range(5):
                            for j in range(5):
                                sqP[i][j] = sq[5 * i + j]

                        # Расшифрование

                        openText1 = cipherT  # Открытый текст
                        cipherSTR = ""
                        simvol = [[], []]
                        slow = []

                        for k in range(len(openText1)):
                            if not openText1[k].isalpha():
                                simvol[0].append(openText1[k])
                                simvol[1].append(k)

                        for k in openText1:
                            if not k.isalpha():
                                openText1 = openText1.replace(k, '')
                        for k in range(len(openText1)):
                            if openText1[k].islower():
                                slow.append(k)
                        openText2 = openText1.upper()

                        for k in range(0, len(openText2), 2):
                            l = [0, 0, 0, 0]
                            for i in range(5):
                                for j in range(5):
                                    if openText2[k] == sqP[i][j]:
                                        l[0] = i
                                        l[1] = j
                                    if openText2[k + 1] == sqP[i][j]:
                                        l[2] = i
                                        l[3] = j
                            if l[1] == l[3]:
                                cipherSTR = cipherSTR + sqP[(l[0] - 1) % 5][l[1]] + sqP[(l[2] - 1) % 5][l[3]]
                            if l[0] == l[2]:
                                cipherSTR = cipherSTR + sqP[l[0]][(l[1] - 1) % 5] + sqP[l[2]][(l[3] - 1) % 5]
                            else:
                                cipherSTR = cipherSTR + sqP[l[0]][l[3]] + sqP[l[2]][l[1]]

                        for i in slow:
                            cipherSTR = cipherSTR[:i] + cipherSTR[i].lower() + cipherSTR[i + 1:]
                        for i in range(len(simvol[0])):
                            cipherSTR = cipherSTR[:int(simvol[1][i])] + simvol[0][i] + cipherSTR[int(simvol[1][i]):]

                        print(cipherSTR)
                        cipherSTR = cipherSTR.replace("X", '')
                        print(cipherSTR)
                        openText.delete(1.0, END)
                        openText.insert(1.0, cipherSTR)


    def polybiusI():
        messagebox.showinfo('Об Квадрате Полибия', 'В криптографии квадрат Полибия (англ. Polybius square), '
                                                   'также известный как шахматная доска Полибия — оригинальный '
                                                   'код простой замены, одна из древнейших систем кодирования, '
                                                   'предложенная Полибием')

    polybiusW = Tk()
    polybiusW.geometry("716x263+322+179")
    polybiusW.title("Шифр Плейфера")
    polybiusW.configure(background="#ffcece")

    openText = Text(polybiusW)
    openText.place(relx=0.029, rely=0.3, relheight=0.612, relwidth=0.37)
    openText.configure(background="white")
    openText.configure(borderwidth="2")
    openText.configure(font="-family {@Malgun Gothic} -size 13")
    openText.configure(foreground="black")

    cipherText = Text(polybiusW)
    cipherText.place(relx=0.601, rely=0.3, relheight=0.612, relwidth=0.37)
    cipherText.configure(background="white")
    cipherText.configure(borderwidth="2")
    cipherText.configure(font="-family {@Malgun Gothic} -size 13")
    cipherText.configure(foreground="black")

    encryptPolybius = Button(polybiusW, command=polybiusE)
    encryptPolybius.place(relx=0.419, rely=0.305, height=34, width=115)
    encryptPolybius.configure(background="#ffffff")
    encryptPolybius.configure(borderwidth="3")
    encryptPolybius.configure(cursor="hand2")
    encryptPolybius.configure(font="-family {@Malgun Gothic} -size 10")
    encryptPolybius.configure(foreground="#000000")
    encryptPolybius.configure(text='''Зашифровать ->''')

    decipherPolybius = Button(polybiusW, command=polybiusD)
    decipherPolybius.place(relx=0.419, rely=0.455, height=34, width=114)
    decipherPolybius.configure(background="#ffffff")
    decipherPolybius.configure(borderwidth="3")
    decipherPolybius.configure(cursor="hand2")
    decipherPolybius.configure(font="-family {@Malgun Gothic} -size 10")
    decipherPolybius.configure(foreground="#000000")
    decipherPolybius.configure(text='''<-Расшифровать''')

    headPolybius = Label(polybiusW)
    headPolybius.place(relx=0.279, rely=0.075, height=52, width=341)
    headPolybius.configure(background="#ffcece")
    headPolybius.configure(font="-family {Open Sans Light} -size 20 -weight bold")
    headPolybius.configure(foreground="#000000")
    headPolybius.configure(text='''Шифр Плейфера''')

    information = Button(polybiusW, command=polybiusI)
    information.place(relx=0.95, rely=0.038, height=24, width=27)
    information.configure(background="#ffffff")
    information.configure(borderwidth="3")
    information.configure(compound='left')
    information.configure(cursor="question_arrow")
    information.configure(font="-family {Segoe UI} -size 11")
    information.configure(foreground="#000000")
    information.configure(text='''?''')

    keyPolybius = Entry(polybiusW)
    keyPolybius.place(relx=0.419, rely=0.602, height=30, relwidth=0.159)
    keyPolybius.configure(background="white")
    keyPolybius.configure(borderwidth="2")
    keyPolybius.configure(font="-family {@Malgun Gothic} -size 14")
    keyPolybius.configure(foreground="#000000")

    headKey = Label(polybiusW)
    headKey.place(relx=0.425, rely=0.714, height=11, width=103)
    headKey.configure(background="#ffcece")
    headKey.configure(font="-family {@Malgun Gothic} -size 8")
    headKey.configure(foreground="#000000")
    headKey.configure(text='''Ключевое слово''')



    TCombobox1 = ttk.Combobox(polybiusW)
    TCombobox1.place(relx=0.768, rely=0.038, relheight=0.079
                          , relwidth=0.158)
    TCombobox1['values'] = ("Русский", "Английский")
    TCombobox1.current(0)  # установите вариант по умолчанию

    polybiusW.mainloop()