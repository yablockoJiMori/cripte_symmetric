from tkinter import *
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import messagebox
from tkinter import filedialog as fd
import re
alfENG='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
alfRUS='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
rus1="а 0.0774\nб 0.0169\nв 0.0479\nг 0.0185\nд 0.0307\nе 0.0839\nё 0.0004\nж 0.0089\nз 0.0166\nи 0.0706\n" \
         "й 0.0155\nк 0.0365\nл 0.0437\nм 0.0321\nн 0.0644\nо 0.1013\nп 0.0305\nр 0.0476\nс 0.0559\nт 0.0625\n" \
         "у 0.0275\nф 0.0029\nх 0.0107\nц 0.0050\nч 0.0140\nш 0.0089\nщ 0.0028\nъ 0.0002\nы 0.0191\nь 0.0171\n" \
         "э 0.0026\nю 0.0073\nя 0.0202\n"
rus2 = "а 0.0698\nб 0.0103\nв 0.0416\nг 0.014\nд 0.0299\nе 0.0968\nё 0.0001\nж 0.0077\nз 0.0151\nи 0.0814\n" \
           "й 0.0105\nк 0.0292\nл 0.0405\nм 0.0343\nн 0.0761\nо 0.1028\nп 0.0287\nр 0.0529\nс 0.0499\nт 0.0653\n" \
           "у 0.0244\nф 0.0071\nх 0.0105\nц 0.007\nч 0.017\nш 0.0042\nщ 0.0043\nъ 0.0002\nы 0.0179\nь 0.0142\n" \
           "э 0.0044\nю 0.0071\nя 0.0250\n"
rus3="а 0.0801\nб 0.0159\nв 0.0454\nг 0.0170\nд 0.0298\nе 0.0845\nё 0.0004\nж 0.0094\nз 0.0165\nи 0.0735\n" \
         "й 0.0121\nк 0.0349\nл 0.0440\nм 0.0321\nн 0.0670\nо 0.1096\nп 0.0281\nр 0.0473\nс 0.0547\nт 0.0626\n" \
         "у 0.0262\nф 0.0026\nх 0.0097\nц 0.0048\nч 0.0144\nш 0.0073\nщ 0.0036\nъ 0.0004\nы 0.0190\nь 0.0174\n" \
         "э 0.0032\nю 0.0064\nя 0.0201\n"
eng="a 0.0812\nb 0.0149\nc 0.0271\nd 0.0432\ne 0.01202\nf 0.0230\ng 0.0203\nh 0.0592\ni 0.0731\nj 0.0010\nk 0.0069\nl 0.0398\nm 0.0261\nn 0.0695\no 0.0768\np 0.0182\nq 0.0011\nr 0.0602\ns 0.0628\nt 0.0910\nu 0.0288\nv 0.0111\nw 0.0209\nx 0.0017\ny 0.0211\nz 0.0007\n"


def freq():
    def choosKey(key):
        key = key.split("\n")
        for i in range(len(key)):
            key[i] = key[i].split(" ")
        for i in range(len(key) - 1):
            key[i][1] = float(key[i][1])

        del key[len(key) - 1]
        sort(key)
        strkey = ""
        for i in range(len(key)):
            strkey = strkey + key[i][0] + " " + str(key[i][1]) + "\n"
        return strkey
    def keyCr():
        language = TCombobox1.get()
        if language == "Русский Обычный":
            key=rus1
        if language == "Русский Технический":
            key = rus2
        if language == "Русский Литературный":
            key = rus3
        if language=="Английский обычный":
            key=eng
        strkey=choosKey(key)
        keyText.delete(1.0, END)
        keyText.insert(1.0, strkey)


    def openF():
        inFile = fd.askopenfilename()
        f = open(inFile, encoding="utf-8")
        # f = open(inFile)
        s = f.read()
        OpenText.delete(1.0, END)
        OpenText.insert(1.0, s)
        f.close()


    def saveF():
        outFile = fd.asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),
                       ("All files", "*.*")))
        f = open(outFile, 'w', encoding="utf-8")
        s = CipherText.get(1.0, END)
        f.write(s)
        f.close()

    def sort(arr):
        def swap(i, j):
            arr[i], arr[j] = arr[j], arr[i]

        n = len(arr)
        swapped = True

        x = -1
        while swapped:
            swapped = False
            x = x + 1
            for i in range(1, n - x):
                if arr[i - 1][1] < arr[i][1]:
                    swap(i - 1, i)
                    swapped = True

    def Freq_count(str):
        language = TCombobox1.get()
        if language == "Английский обычный":
            openMass = [["q", 0], ["w", 0], ["e", 0], ["r", 0], ["t", 0], ["y", 0], ["u", 0], ["i", 0], ["o", 0],
            ["p", 0],
            ["a", 0], ["s", 0], ["d", 0], ["f", 0], ["g", 0], ["h", 0], ["j", 0], ["k", 0], ["l", 0],
            ["z", 0],
            ["x", 0], ["c", 0], ["v", 0], ["b", 0], ["n", 0], ["m", 0]]
        else:
            openMass = [["й", 0], ["ц", 0], ["у", 0], ["к", 0], ["е", 0], ["н", 0], ["г", 0], ["ш", 0], ["щ", 0],
            ["з", 0],
            ["х", 0], ["ъ", 0], ["ф", 0], ["ы", 0], ["в", 0], ["а", 0], ["п", 0], ["р", 0], ["о", 0],
            ["л", 0],
            ["д", 0], ["ж", 0], ["э", 0], ["я", 0], ["ч", 0], ["с", 0], ["м", 0], ["и", 0], ["т", 0],
            ["б", 0],
            ["ю", 0], ["ь", 0], ["ё", 0]]
        for j in range(len(openMass)):

            for i in range(len(str)):
                if str[i] == openMass[j][0]:
                    openMass[j][1] += 1
            print(openMass[j][0],openMass[j][1])
        for j in range(len(openMass)):
            openMass[j][1] = openMass[j][1] / len(str)
        return openMass

    def decipher():
        OpenSTR1 = OpenText.get(1.0, END)
        OpenSTR = OpenSTR1[:-1]
        key = keyText.get(1.0, END)
        key = key[:-1]
        if not re.match(r"^([a-zA-Zа-яА-ЯёЁ] \d+[.]\d+\n)+$", key):
            messagebox.showerror('Ошибка', 'Неверный ключ1.')
        else:
            key = key.split("\n")
            for i in range(len(key)):
                key[i] = key[i].split(" ")
            for i in range(len(key) - 1):
                key[i][1] = float(key[i][1])

            del key[len(key) - 1]
            sort(key)

            simvol = [[], []]

            language = TCombobox1.get()
            if language == "Английский обычный":
                alf = alfENG
            else:
                alf = alfRUS

            for k in range(len(OpenSTR)):
                if not (OpenSTR[k] in alf):
                    simvol[0].append(OpenSTR[k])
                    simvol[1].append(k)
            print("символы")
            for k in OpenSTR:
                if not (k in alf):
                    OpenSTR = OpenSTR.replace(k, '')

            OpenSTR = OpenSTR.lower()
            print("подъем")
            openMass=Freq_count(OpenSTR)
            sort(openMass)

            chithSTR = ""
            for i in range(len(OpenSTR)):
                for j in range(len(openMass)):
                    if OpenSTR[i] == openMass[j][0]:
                        chithSTR = chithSTR + key[j][0]
            print("шифр")
            for i in range(len(simvol[0])):
                chithSTR = chithSTR[:int(simvol[1][i])] + simvol[0][i] + chithSTR[int(simvol[1][i]):]
            print("символы")


            for i in range(len(chithSTR)):
                if OpenSTR1[i].isupper() and (OpenSTR1[i] in alfRUS):
                    chithSTR = chithSTR[:i] + chithSTR[i].upper() + chithSTR[i + 1:]

            CipherText.delete(1.0, END)
            CipherText.insert(1.0, chithSTR)



    freqW = Tk()
    freqW.geometry("832x584+273+108")
    freqW.minsize(120, 1)
    freqW.maxsize(1444, 941)
    freqW.resizable(1, 1)
    freqW.title("freqWlevel 0")
    freqW.configure(background="#e6fdff")

    keyText = Text(freqW)
    keyText.place(relx=0.024, rely=0.034, relheight=0.932, relwidth=0.113)

    keyText.configure(background="white")
    keyText.configure(font="TkTextFont")
    keyText.configure(foreground="black")
    keyText.configure(highlightbackground="#d9d9d9")
    keyText.configure(highlightcolor="black")
    keyText.configure(insertbackground="black")
    keyText.configure(selectbackground="#c4c4c4")
    keyText.configure(selectforeground="black")
    keyText.configure(wrap="word")

    OpenText = Text(freqW)
    OpenText.place(relx=0.337, rely=0.034, relheight=0.435, relwidth=0.631)

    OpenText.configure(background="white")
    OpenText.configure(font="TkTextFont")
    OpenText.configure(foreground="black")
    OpenText.configure(highlightbackground="#d9d9d9")
    OpenText.configure(highlightcolor="black")
    OpenText.configure(insertbackground="black")
    OpenText.configure(selectbackground="#c4c4c4")
    OpenText.configure(selectforeground="black")
    OpenText.configure(wrap="word")

    CipherText = Text(freqW)
    CipherText.place(relx=0.337, rely=0.497, relheight=0.469, relwidth=0.631)

    CipherText.configure(background="white")
    CipherText.configure(font="TkTextFont")
    CipherText.configure(foreground="black")
    CipherText.configure(highlightbackground="#d9d9d9")
    CipherText.configure(highlightcolor="black")
    CipherText.configure(insertbackground="black")
    CipherText.configure(selectbackground="#c4c4c4")
    CipherText.configure(selectforeground="black")
    CipherText.configure(wrap="word")

    keyB = Button(freqW, command=keyCr)
    keyB.place(relx=0.168, rely=0.103, height=34, width=127)
    keyB.configure(activebackground="beige")
    keyB.configure(activeforeground="#000000")
    keyB.configure(background="#e9e9e9")
    keyB.configure(compound='left')
    keyB.configure(disabledforeground="#a3a3a3")
    keyB.configure(foreground="#000000")
    keyB.configure(highlightbackground="#d9d9d9")
    keyB.configure(highlightcolor="black")
    keyB.configure(pady="0")
    keyB.configure(text='''Выбрать алфавит''')

    InB = Button(freqW, command=openF)
    InB.place(relx=0.168, rely=0.274, height=34, width=127)
    InB.configure(activebackground="beige")
    InB.configure(activeforeground="#000000")
    InB.configure(background="#e9e9e9")
    InB.configure(compound='left')
    InB.configure(disabledforeground="#a3a3a3")
    InB.configure(foreground="#000000")
    InB.configure(highlightbackground="#d9d9d9")
    InB.configure(highlightcolor="black")
    InB.configure(pady="0")
    InB.configure(text='''Открыть файл''')

    OutB = Button(freqW, command=saveF)
    OutB.place(relx=0.168, rely=0.702, height=34, width=127)
    OutB.configure(activebackground="beige")
    OutB.configure(activeforeground="#000000")
    OutB.configure(background="#e9e9e9")
    OutB.configure(compound='left')
    OutB.configure(disabledforeground="#a3a3a3")
    OutB.configure(foreground="#000000")
    OutB.configure(highlightbackground="#d9d9d9")
    OutB.configure(highlightcolor="black")
    OutB.configure(pady="0")
    OutB.configure(text='''Сохранить файл''')

    Decript = Button(freqW, command=decipher)
    Decript.place(relx=0.168, rely=0.89, height=34, width=127)
    Decript.configure(activebackground="beige")
    Decript.configure(activeforeground="#000000")
    Decript.configure(background="#e9e9e9")
    Decript.configure(compound='left')
    Decript.configure(disabledforeground="#a3a3a3")
    Decript.configure(foreground="#000000")
    Decript.configure(highlightbackground="#d9d9d9")
    Decript.configure(highlightcolor="black")
    Decript.configure(pady="0")
    Decript.configure(text='''Дешифровать''')

    TCombobox1 = ttk.Combobox(freqW)
    TCombobox1.place(relx=0.168, rely=0.034, relheight=0.053, relwidth=0.148)
    TCombobox1['values'] = ("Русский Обычный","Русский Технический","Русский Литературный", "Английский обычный")
    TCombobox1.current(0)

    freqW.mainloop()