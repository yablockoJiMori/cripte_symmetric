from tkinter import *
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import messagebox
from tkinter import filedialog as fd
from scipy.stats import chisquare
from math import ceil
alfENG='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
alfRUS='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabetRUSlo = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabetENGlo='abcdefghijklmnopqrstuvwxyz'
RUS = [8.01,1.59,  4.54, 1.70,  2.98, 8.45,  0.04, 0.94,  1.65,  7.35,  1.21,   3.49,4.40,  3.21, 6.70, 10.96,  2.81,   4.73,  5.47,  6.26,   2.62, 0.26,  0.97,  0.48,  1.44,  0.73, 0.36,  0.04, 1.90, 1.74, 0.32,0.64, 2.01]
ENG = [8.12, 1.49,  2.71,   4.32,   12.02, 2.30,  2.03, 5.92,   7.31,   0.10,  0.69,  3.98, 2.61, 6.95, 7.68,   1.82,   0.11,  6.02,   6.28,  9.10,  2.88, 1.11,  2.09, 0.17,   2.11,   0.07]


def anAuto():
    def Freq_count(str, shift):
        openM = []
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
        for i in range(len(openMass)):
            openM.append(openMass[i][1])
        return openM

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
            FRE=RUS
        elif language == "Английский":
            alf = alfENG
            alflo = alphabetENGlo
            sizeA = 33
            indA=0.064
            FRE = ENG
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

        tmpKey = []
        for i in range(1, len(openSTR) // 2):
            ind = 0
            openSTRshift = (openSTR[i:])
            flac = 0
            for j in range(len(openSTRshift)):
                if openSTRshift[j] == openSTR[j]:
                    flac += 1
            ind = flac / len(openSTRshift)
            # print(ind)
            if ind > indA:
                tmpKey.append(i)
        sum = 0
        for i in range(1, len(tmpKey)):
            sum += (tmpKey[i] - tmpKey[i - 1])
        #key=ceil(sum / (len(tmpKey) - 1))
        key = sum / (len(tmpKey) - 1)
        tmpkeyE.delete(0, END)
        tmpkeyE.insert(0, str(tmpKey))
        sizeE.delete(0, END)
        sizeE.insert(0, str(key))

    def makeKey():
        openSTR = openText.get(1.0, END)
        openSTR = openSTR[:-1]
        language = TCombobox1.get()
        if language == "Русский":
            alf = alfRUS
            alflo = alphabetRUSlo
            sizeA = 33
            indA = 0.05
            FRE = RUS
        elif language == "Английский":
            alf = alfENG
            alflo = alphabetENGlo
            sizeA = 26
            indA = 0.064
            FRE = ENG
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

        sizeKey=sizeE.get()
        if not sizeKey.isdigit():
            messagebox.showerror('Ошибка', 'Неверная длина.')
        else:
            sizeKey=int(sizeKey)
            keyDit = []
            for k in range(sizeKey):
                str1 = ""
                for i in range(k, len(openSTR), sizeKey):
                    str1 += openSTR[i]
                minCHI = 9999999999
                minShift = 0
                for k in range(sizeA):
                    str2 = ""
                    indMut = 0
                    for i in range(len(str1)):
                        for j in range(len(alflo)):
                            if str1[i] == alflo[j]:
                                str2 += alflo[(j + k) % sizeA]
                    FREnorm = [0] * sizeA
                    sum1=0
                    for i in range(len(FRE)):
                        FREnorm[i] = (FRE[i] / 100) * len(str2)
                        sum1+=FREnorm[i]
                    tmp=Freq_count(str2, 1)
                    sum2=0
                    for i in range(len(tmp)):
                        sum2+=tmp[i]

                    FREnorm[0]=FREnorm[0]-(sum1-sum2)



                    CHI = chisquare(Freq_count(str2, 1), FREnorm).statistic
                    # print(CHI)
                    if CHI < minCHI:
                        minCHI = CHI
                        minShift = sizeA - k


                keyDit.append(minShift)
            key = ""
            for i in range(len(keyDit)):
                key += alflo[keyDit[i]]

            Entry1.delete(0, END)
            Entry1.insert(0, key)


    autoW=Tk()
    autoW.geometry("648x515+353+185")
    autoW.minsize(120, 1)
    autoW.maxsize(1444, 941)
    autoW.resizable(1, 1)
    autoW.title("Автокорреляционный метод")
    autoW.configure(background="#e6fdff")
    autoW.configure(highlightbackground="#d9d9d9")
    autoW.configure(highlightcolor="black")


    fileE = Entry(autoW)
    fileE.place(relx=0.015, rely=0.078, height=30, relwidth=0.778)
    fileE.configure(background="white")
    fileE.configure(disabledforeground="#a3a3a3")
    fileE.configure(font="-family {Courier New} -size 12")
    fileE.configure(foreground="#000000")
    fileE.configure(highlightbackground="#d9d9d9")
    fileE.configure(highlightcolor="black")
    fileE.configure(insertbackground="black")
    fileE.configure(selectbackground="#c4c4c4")
    fileE.configure(selectforeground="black")

    openB = Button(autoW, command=openF)
    openB.place(relx=0.818, rely=0.078, height=34, width=97)
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

    TCombobox1 = ttk.Combobox(autoW)
    TCombobox1.place(relx=0.787, rely=0.019, relheight=0.049
                     , relwidth=0.184)
    TCombobox1.configure(font="-family {Segoe UI} -size 12")
    TCombobox1.configure(takefocus="")
    TCombobox1['values'] = ("Русский", "Английский")
    TCombobox1.current(0)

    tmpkeyE = Entry(autoW)
    tmpkeyE.place(relx=0.015, rely=0.738, height=30, relwidth=0.762)
    tmpkeyE.configure(background="white")
    tmpkeyE.configure(disabledforeground="#a3a3a3")
    tmpkeyE.configure(font="-family {Courier New} -size 12")
    tmpkeyE.configure(foreground="#000000")
    tmpkeyE.configure(highlightbackground="#d9d9d9")
    tmpkeyE.configure(highlightcolor="black")
    tmpkeyE.configure(insertbackground="black")
    tmpkeyE.configure(selectbackground="#c4c4c4")
    tmpkeyE.configure(selectforeground="black")

    Label1 = Label(autoW)
    Label1.place(relx=0.015, rely=0.019, height=29, width=112)
    Label1.configure(activebackground="#f9f9f9")
    Label1.configure(anchor='w')
    Label1.configure(background="#e6fdff")
    Label1.configure(compound='left')
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(font="-family {Segoe UI} -size 13")
    Label1.configure(foreground="#000000")
    Label1.configure(highlightbackground="#d9d9d9")
    Label1.configure(highlightcolor="black")
    Label1.configure(text='''Путь к файлу''')

    Label2 = Label(autoW)
    Label2.place(relx=0.015, rely=0.66, height=27, width=493)
    Label2.configure(activebackground="#f9f9f9")
    Label2.configure(anchor='w')
    Label2.configure(background="#e6fdff")
    Label2.configure(compound='left')
    Label2.configure(disabledforeground="#a3a3a3")
    Label2.configure(font="-family {Segoe UI} -size 13")
    Label2.configure(foreground="#000000")
    Label2.configure(highlightbackground="#d9d9d9")
    Label2.configure(highlightcolor="black")
    Label2.configure(text='''Значения, которым предположительно кратна длина ключа''')

    Label3 = Label(autoW)
    Label3.place(relx=0.015, rely=0.816, height=31, width=123)
    Label3.configure(activebackground="#f9f9f9")
    Label3.configure(anchor='w')
    Label3.configure(background="#e6fdff")
    Label3.configure(compound='left')
    Label3.configure(disabledforeground="#a3a3a3")
    Label3.configure(font="-family {Segoe UI} -size 13")
    Label3.configure(foreground="#000000")
    Label3.configure(highlightbackground="#d9d9d9")
    Label3.configure(highlightcolor="black")
    Label3.configure(text='''Длина ключа''')

    sizeE = Entry(autoW)
    sizeE.place(relx=0.015, rely=0.893, height=30, relwidth=0.176)
    sizeE.configure(background="white")
    sizeE.configure(disabledforeground="#a3a3a3")
    sizeE.configure(font="-family {Courier New} -size 12")
    sizeE.configure(foreground="#000000")
    sizeE.configure(highlightbackground="#d9d9d9")
    sizeE.configure(highlightcolor="black")
    sizeE.configure(insertbackground="black")
    sizeE.configure(selectbackground="#c4c4c4")
    sizeE.configure(selectforeground="black")

    tmpkeyB = Button(autoW, command=makeSize)
    tmpkeyB.place(relx=0.802, rely=0.718, height=34, width=97)
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

    keyB = Button(autoW, command=makeKey)
    keyB.place(relx=0.247, rely=0.835, height=64, width=97)
    keyB.configure(activebackground="beige")
    keyB.configure(activeforeground="#000000")
    keyB.configure(background="#e9e9e9")
    keyB.configure(compound='left')
    keyB.configure(disabledforeground="#a3a3a3")
    keyB.configure(foreground="#000000")
    keyB.configure(highlightbackground="#d9d9d9")
    keyB.configure(highlightcolor="black")
    keyB.configure(pady="0")
    keyB.configure(text='''Найти ключ''')

    Label4 = Label(autoW)
    Label4.place(relx=0.633, rely=0.796, height=41, width=144)
    Label4.configure(activebackground="#f9f9f9")
    Label4.configure(anchor='w')
    Label4.configure(background="#e6fdff")
    Label4.configure(compound='left')
    Label4.configure(disabledforeground="#a3a3a3")
    Label4.configure(font="-family {Segoe UI} -size 11")
    Label4.configure(foreground="#000000")
    Label4.configure(highlightbackground="#d9d9d9")
    Label4.configure(highlightcolor="black")
    Label4.configure(text='''Возможный ключ''')

    Entry1 = Entry(autoW)
    Entry1.place(relx=0.633, rely=0.874, height=40, relwidth=0.207)
    Entry1.configure(background="white")
    Entry1.configure(disabledforeground="#a3a3a3")
    Entry1.configure(font="-family {Courier New} -size 12")
    Entry1.configure(foreground="#000000")
    Entry1.configure(insertbackground="black")

    openText = Text(autoW)
    openText.place(relx=0.015, rely=0.155, relheight=0.493, relwidth=0.948)
    openText.configure(background="white")
    openText.configure(font="-family {Courier New} -size 12")
    openText.configure(foreground="black")
    openText.configure(highlightbackground="#d9d9d9")
    openText.configure(highlightcolor="black")
    openText.configure(insertbackground="black")
    openText.configure(selectbackground="#c4c4c4")
    openText.configure(selectforeground="black")
    openText.configure(wrap="word")

    autoW.mainloop()