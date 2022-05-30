from tkinter import *
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import messagebox
from tkinter import filedialog as fd
alfENG='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
alfRUS='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabetRUSlo = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabetENGlo='abcdefghijklmnopqrstuvwxyz'


def anIndex():
    def Freq_count(str, shift):
        language = TCombobox1.get()
        if language == "Английский":
            openMass = [["a", 0], ["b", 0], ["c", 0], ["d", 0], ["e", 0], ["f", 0], ["g", 0], ["h", 0], ["i", 0],
                    ["j", 0],
                    ["k", 0], ["l", 0], ["m", 0], ["n", 0], ["o", 0], ["p", 0], ["q", 0], ["r", 0], ["s", 0],
                    ["t", 0],
                    ["u", 0], ["v", 0], ["w", 0], ["x", 0], ["y", 0], ["z", 0]]
        if language == "Русский":
            openMass = [["а", 0], ["б", 0], ["в", 0], ["г", 0], ["д", 0], ["е", 0], ["ё", 0], ["ж", 0], ["з", 0],
                        ["и", 0],
                        ["й", 0], ["к", 0], ["л", 0], ["м", 0], ["н", 0], ["о", 0], ["п", 0], ["р", 0], ["с", 0],
                        ["т", 0],
                        ["у", 0], ["ф", 0], ["х", 0], ["ц", 0], ["ч", 0], ["ш", 0], ["щ", 0], ["ъ", 0], ["ы", 0],
                        ["ь", 0],
                        ["э", 0], ["ю", 0], ["я", 0]]
        for j in range(len(openMass)):

            for i in range(0, len(str), shift):
                if str[i] == openMass[j][0]:
                    openMass[j][1] += 1

        return openMass

    def openF():
        inFile = fd.askopenfilename()
        fileE.delete(0, END)
        fileE.insert(0, inFile)
        f = open(inFile, encoding="utf-8")
        # f = open(inFile, encoding="utf-8")
        s = f.read()
        openText.delete(1.0, END)
        openText.insert(1.0, s)
        f.close()

    def makeSize():
        openSTR = openText.get(1.0, END)
        openSTR = openSTR[:-1]
        language = TCombobox1.get()
        if language == "Русский":
            alf=alfRUS
            alflo=alphabetRUSlo
            sizeA=33
            indA=0.05
        elif language == "Английский":
            alf = alfENG
            alflo = alphabetENGlo
            sizeA = 26
            indA=0.064
        else:
            messagebox.showerror('Ошибка', 'Неверный язык.')

        simvol = [[], []]
        for k in range(len(openSTR)):
            if not (openSTR[k] in alf):
                simvol[0].append(openSTR[k])
                simvol[1].append(k)
        for k in openSTR:
            if not (k in alf):
                openSTR = openSTR.replace(k, '')

        openSTR = openSTR.lower()
        ind = 0
        tmpKey = []
        shift = 1
        for i in range(len(openSTR) - 1):
            openMass = Freq_count(openSTR, shift)
            ind = 0
            size = len(openSTR) / shift
            for i in range(len(openMass)):
                ind += (openMass[i][1] * (openMass[i][1] - 1)) / (size * (size - 1))
            if ind > indA:
                tmpKey.append(shift)
            # print(ind)
            shift += 1
        tmpkeyE.delete(0, END)
        tmpkeyE.insert(0, str(tmpKey))
        sizeE.delete(0, END)
        sizeE.insert(0, str(tmpKey[0]))

    def makeKey():
        openSTR = openText.get(1.0, END)
        openSTR = openSTR[:-1]
        language = TCombobox1.get()
        if language == "Русский":
            alf = alfRUS
            alflo = alphabetRUSlo
            sizeA = 33
            indA = 0.05
        elif language == "Английский":
            alf = alfENG
            alflo = alphabetENGlo
            sizeA = 26
            indA = 0.064
        else:
            messagebox.showerror('Ошибка', 'Неверный язык.')

        simvol = [[], []]
        for k in range(len(openSTR)):
            if not (openSTR[k] in alf):
                simvol[0].append(openSTR[k])
                simvol[1].append(k)
        for k in openSTR:
            if not (k in alf):
                openSTR = openSTR.replace(k, '')
        openSTR = openSTR.lower()

        shift=sizeE.get()
        if not shift.isdigit():
            messagebox.showerror('Ошибка', 'Неверная длина.')
        else:
            shift = int(shift)+1
            str = ""
            for i in range(0, len(openSTR), shift - 1):
                str += openSTR[i]
            keyShift = []
            for k in range(1, shift - 1):
                str1 = ""
                for i in range(k, len(openSTR), shift - 1):
                    str1 += openSTR[i]
                indMut = 0
                str2 = ""
                shift2 = 0
                alfShift = []
                f = 0
                while indMut < indA and f < sizeA:
                    str2 = ""
                    indMut = 0
                    for i in range(len(str1)):
                        for j in range(len(alflo)):
                            if str1[i] == alflo[j]:
                                str2 += alflo[(j + shift2) % sizeA]
                    openMass = Freq_count(str, 1)
                    openMass2 = Freq_count(str2, 1)
                    for i in range(len(openMass2)):
                        indMut += (openMass[i][1] * openMass2[i][1]) / (len(str) * len(str2))
                    f += 1
                    shift2 += 1
                if f == sizeA:
                    messagebox.showerror('Ошибка', 'Неверная длина кодового слова.')
                    raise Exception('Неверная длина кодового слова')
                    break
                keyShift.append(shift2 - 1)

            keys.delete(1.0, END)
            for i in range(sizeA):
                key = alflo[i]
                for k in range(len(keyShift)):
                    key += alflo[(i - int(keyShift[k])) % sizeA]
                keys.insert(1.0, "\n")
                keys.insert(1.0, key)
                #print(key)






    indW=Tk()
    indW.geometry("649x463+375+237")
    indW.minsize(120, 1)
    indW.maxsize(1444, 941)
    indW.resizable(1, 1)
    indW.title("Метод идекса совпадений")
    indW.configure(background="#e6fdff")


    fileE = Entry(indW)
    fileE.place(relx=0.015, rely=0.086, height=30, relwidth=0.561)
    fileE.configure(background="white")
    fileE.configure(disabledforeground="#a3a3a3")
    fileE.configure(font="-family {Courier New} -size 12")
    fileE.configure(foreground="#000000")
    fileE.configure(insertbackground="black")

    openB = Button(indW, command=openF)
    openB.place(relx=0.602, rely=0.086, height=24, width=97)
    openB.configure(activebackground="beige")
    openB.configure(activeforeground="#000000")
    openB.configure(background="#e9e9e9")
    openB.configure(compound='left')
    openB.configure(disabledforeground="#a3a3a3")
    openB.configure(foreground="#000000")
    openB.configure(highlightbackground="#d9d9d9")
    openB.configure(highlightcolor="black")
    openB.configure(pady="0")
    openB.configure(text='''Выбрать файл''')

    TCombobox1 = ttk.Combobox(indW)
    TCombobox1.place(relx=0.401, rely=0.821, relheight=0.145, relwidth=0.185)
    TCombobox1.configure(font="-family {Segoe UI} -size 12")
    TCombobox1.configure(takefocus="")
    TCombobox1['values'] = ("Русский", "Английский")
    TCombobox1.current(0)

    tmpkeyE = Entry(indW)
    tmpkeyE.place(relx=0.015, rely=0.713, height=30, relwidth=0.561)
    tmpkeyE.configure(background="white")
    tmpkeyE.configure(disabledforeground="#a3a3a3")
    tmpkeyE.configure(font="-family {Courier New} -size 12")
    tmpkeyE.configure(foreground="#000000")
    tmpkeyE.configure(insertbackground="black")

    Label1 = Label(indW)
    Label1.place(relx=0.031, rely=0.022, height=25, width=123)
    Label1.configure(anchor='w')
    Label1.configure(background="#e6fdff")
    Label1.configure(compound='left')
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(font="-family {Segoe UI} -size 13")
    Label1.configure(foreground="#000000")
    Label1.configure(text='''Путь к файлу''')

    Label2 = Label(indW)
    Label2.place(relx=0.015, rely=0.648, height=21, width=494)
    Label2.configure(anchor='w')
    Label2.configure(background="#e6fdff")
    Label2.configure(compound='left')
    Label2.configure(disabledforeground="#a3a3a3")
    Label2.configure(font="-family {Segoe UI} -size 13")
    Label2.configure(foreground="#000000")
    Label2.configure(text='''Значения, которым предположительно кратна длина ключа''')

    Label3 = Label(indW)
    Label3.place(relx=0.015, rely=0.778, height=63, width=123)
    Label3.configure(anchor='w')
    Label3.configure(background="#e6fdff")
    Label3.configure(compound='left')
    Label3.configure(disabledforeground="#a3a3a3")
    Label3.configure(font="-family {Segoe UI} -size 13")
    Label3.configure(foreground="#000000")
    Label3.configure(text='''Длина ключа''')

    sizeE = Entry(indW)
    sizeE.place(relx=0.015, rely=0.886, height=30, relwidth=0.176)
    sizeE.configure(background="white")
    sizeE.configure(disabledforeground="#a3a3a3")
    sizeE.configure(font="-family {Courier New} -size 12")
    sizeE.configure(foreground="#000000")
    sizeE.configure(insertbackground="black")

    tmpkeyB = Button(indW, command=makeSize)
    tmpkeyB.place(relx=0.602, rely=0.713, height=24, width=97)
    tmpkeyB.configure(activebackground="beige")
    tmpkeyB.configure(activeforeground="#000000")
    tmpkeyB.configure(background="#e9e9e9")
    tmpkeyB.configure(compound='left')
    tmpkeyB.configure(disabledforeground="#a3a3a3")
    tmpkeyB.configure(foreground="#000000")
    tmpkeyB.configure(highlightbackground="#d9d9d9")
    tmpkeyB.configure(highlightcolor="black")
    tmpkeyB.configure(pady="0")
    tmpkeyB.configure(text='''Найти значения''')

    keyB = Button(indW, command=makeKey)
    keyB.place(relx=0.216, rely=0.821, height=64, width=97)
    keyB.configure(activebackground="beige")
    keyB.configure(activeforeground="#000000")
    keyB.configure(background="#e9e9e9")
    keyB.configure(compound='left')
    keyB.configure(disabledforeground="#a3a3a3")
    keyB.configure(foreground="#000000")
    keyB.configure(highlightbackground="#d9d9d9")
    keyB.configure(highlightcolor="black")
    keyB.configure(pady="0")
    keyB.configure(text='''Найти ключи''')

    keys = Text(indW)
    keys.place(relx=0.801, rely=0.086, relheight=0.875, relwidth=0.16)
    keys.configure(background="white")
    keys.configure(font="-family {Segoe UI} -size 12")
    keys.configure(foreground="black")
    keys.configure(highlightbackground="#d9d9d9")
    keys.configure(highlightcolor="black")
    keys.configure(insertbackground="black")
    keys.configure(selectbackground="#c4c4c4")
    keys.configure(selectforeground="black")
    keys.configure(wrap="word")

    Label4 = Label(indW)
    Label4.place(relx=0.772, rely=0.0, height=37, width=144)
    Label4.configure(anchor='w')
    Label4.configure(background="#e6fdff")
    Label4.configure(compound='left')
    Label4.configure(disabledforeground="#a3a3a3")
    Label4.configure(font="-family {Segoe UI} -size 11")
    Label4.configure(foreground="#000000")
    Label4.configure(text='''Возможные ключи''')

    openText = Text(indW)
    openText.place(relx=0.015, rely=0.173, relheight=0.441, relwidth=0.73)
    openText.configure(background="white")
    openText.configure(font="-family {Courier New} -size 12")
    openText.configure(foreground="black")
    openText.configure(highlightbackground="#d9d9d9")
    openText.configure(highlightcolor="black")
    openText.configure(insertbackground="black")
    openText.configure(selectbackground="#c4c4c4")
    openText.configure(selectforeground="black")
    openText.configure(wrap="word")

    indW.mainloop()