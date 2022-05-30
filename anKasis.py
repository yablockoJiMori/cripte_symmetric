from tkinter import *
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import messagebox
from tkinter import filedialog as fd
from math import gcd
alfENG='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
alfRUS='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'



def anKas():

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

        elif language == "Английский":
            alf = alfENG

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

        lenD = sizeE.get()
        limit=Entry1_1.get()
        if not lenD.isdigit() or not limit.isdigit():
            messagebox.showerror('Ошибка', 'Неверная длина.')
        else:
            lenD = int(lenD)
            limit = int(limit)
            dict = {}
            for i, letter in enumerate(openSTR):
                seq = openSTR[i:i + lenD]
                if seq in dict.keys():
                    dict[seq].append(i)
                else:
                    dict[seq] = [i]
            filterDict = {key: dict[key] for key in
                          filter(lambda x: len(dict[x]) >= limit, dict)}

            dict = filterDict
            tmpKey = set()
            for positions in dict.values():
                distances = [0] * (len(positions) - 1)
                for i in range(len(positions) - 1):
                    distances[i] = positions[i + 1] - positions[i]
                possible_len = gcd(*distances)
                if 3 <= possible_len <= 20:
                    tmpKey.add(possible_len)
            tmpKey = sorted(tmpKey)
            tmpkeyE.delete(0, END)
            tmpkeyE.insert(0, str(tmpKey))

    anKasW=Tk()
    anKasW.geometry("648x526+353+185")
    anKasW.minsize(120, 1)
    anKasW.maxsize(1444, 941)
    anKasW.resizable(1, 1)
    anKasW.title("Тест Казиски ")
    anKasW.configure(background="#e6fdff")
    anKasW.configure(highlightbackground="#d9d9d9")
    anKasW.configure(highlightcolor="black")

    fileE = Entry(anKasW)
    fileE.place(relx=0.015, rely=0.095, height=30, relwidth=0.562)
    fileE.configure(background="white")
    fileE.configure(disabledforeground="#a3a3a3")
    fileE.configure(font="-family {Courier New} -size 12")
    fileE.configure(foreground="#000000")
    fileE.configure(highlightbackground="#d9d9d9")
    fileE.configure(highlightcolor="black")
    fileE.configure(insertbackground="black")
    fileE.configure(selectbackground="#c4c4c4")
    fileE.configure(selectforeground="black")

    openB = Button(anKasW, command=openF)
    openB.place(relx=0.602, rely=0.095, height=24, width=97)
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

    TCombobox1 = ttk.Combobox(anKasW)
    TCombobox1.place(relx=0.772, rely=0.095, relheight=0.049
                     , relwidth=0.184)
    TCombobox1.configure(font="-family {Segoe UI} -size 12")
    TCombobox1.configure(takefocus="")
    TCombobox1['values'] = ("Русский", "Английский")
    TCombobox1.current(0)

    tmpkeyE = Entry(anKasW)
    tmpkeyE.place(relx=0.015, rely=0.913, height=30, relwidth=0.562)
    tmpkeyE.configure(background="white")
    tmpkeyE.configure(disabledforeground="#a3a3a3")
    tmpkeyE.configure(font="-family {Courier New} -size 12")
    tmpkeyE.configure(foreground="#000000")
    tmpkeyE.configure(highlightbackground="#d9d9d9")
    tmpkeyE.configure(highlightcolor="black")
    tmpkeyE.configure(insertbackground="black")
    tmpkeyE.configure(selectbackground="#c4c4c4")
    tmpkeyE.configure(selectforeground="black")

    Label1 = Label(anKasW)
    Label1.place(relx=0.015, rely=0.038, height=20, width=112)
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

    Label2 = Label(anKasW)
    Label2.place(relx=0.015, rely=0.856, height=28, width=223)
    Label2.configure(activebackground="#f9f9f9")
    Label2.configure(anchor='w')
    Label2.configure(background="#e6fdff")
    Label2.configure(compound='left')
    Label2.configure(disabledforeground="#a3a3a3")
    Label2.configure(font="-family {Segoe UI} -size 13")
    Label2.configure(foreground="#000000")
    Label2.configure(highlightbackground="#d9d9d9")
    Label2.configure(highlightcolor="black")
    Label2.configure(text='''Возможные длины ключа''')

    Label3 = Label(anKasW)
    Label3.place(relx=0.015, rely=0.171, height=32, width=252)
    Label3.configure(activebackground="#f9f9f9")
    Label3.configure(anchor='w')
    Label3.configure(background="#e6fdff")
    Label3.configure(compound='left')
    Label3.configure(disabledforeground="#a3a3a3")
    Label3.configure(font="-family {Segoe UI} -size 13")
    Label3.configure(foreground="#000000")
    Label3.configure(highlightbackground="#d9d9d9")
    Label3.configure(highlightcolor="black")
    Label3.configure(text='''Длина подстроки повторения''')

    sizeE = Entry(anKasW)
    sizeE.place(relx=0.401, rely=0.171, height=30, relwidth=0.099)
    sizeE.configure(background="white")
    sizeE.configure(cursor="fleur")
    sizeE.configure(disabledforeground="#a3a3a3")
    sizeE.configure(font="-family {Courier New} -size 12")
    sizeE.configure(foreground="#000000")
    sizeE.configure(highlightbackground="#d9d9d9")
    sizeE.configure(highlightcolor="black")
    sizeE.configure(insertbackground="black")
    sizeE.configure(selectbackground="#c4c4c4")
    sizeE.configure(selectforeground="black")
    sizeE.insert(0, "3")

    tmpkeyB = Button(anKasW, command=makeSize)
    tmpkeyB.place(relx=0.617, rely=0.913, height=24, width=227)
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


    Entry1_1 = Entry(anKasW)
    Entry1_1.place(relx=0.864, rely=0.171, height=30, relwidth=0.099)
    Entry1_1.configure(background="white")
    Entry1_1.configure(disabledforeground="#a3a3a3")
    Entry1_1.configure(font="TkFixedFont")
    Entry1_1.configure(foreground="#000000")
    Entry1_1.configure(highlightbackground="#d9d9d9")
    Entry1_1.configure(highlightcolor="black")
    Entry1_1.configure(insertbackground="black")
    Entry1_1.configure(selectbackground="#c4c4c4")
    Entry1_1.configure(selectforeground="black")
    Entry1_1.insert(0, "3")

    Label3_1 = Label(anKasW)
    Label3_1.place(relx=0.54, rely=0.171, height=22, width=202)
    Label3_1.configure(activebackground="#f9f9f9")
    Label3_1.configure(anchor='w')
    Label3_1.configure(background="#e6fdff")
    Label3_1.configure(compound='left')
    Label3_1.configure(cursor="fleur")
    Label3_1.configure(disabledforeground="#a3a3a3")
    Label3_1.configure(font="-family {Segoe UI} -size 13")
    Label3_1.configure(foreground="#000000")
    Label3_1.configure(highlightbackground="#d9d9d9")
    Label3_1.configure(highlightcolor="black")
    Label3_1.configure(text='''Количество повторений''')

    openText = Text(anKasW)
    openText.place(relx=0.015, rely=0.247, relheight=0.597, relwidth=0.948)
    openText.configure(background="white")
    openText.configure(font="-family {Courier New} -size 12")
    openText.configure(foreground="black")
    openText.configure(highlightbackground="#d9d9d9")
    openText.configure(highlightcolor="black")
    openText.configure(insertbackground="black")
    openText.configure(selectbackground="#c4c4c4")
    openText.configure(selectforeground="black")
    openText.configure(wrap="word")

    anKasW.mainloop()