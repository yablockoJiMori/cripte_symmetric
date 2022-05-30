from tkinter import *
from tkinter.constants import *
from tkinter import messagebox
from tkinter import filedialog as fd
def gamma():
    def openF():
        inFile = fd.askopenfilename()
        Entry1.delete(0, END)
        Entry1.insert(0, inFile)
    def saveF():
        inFile = Entry1.get()

        for i in range(len(inFile)-1, 0, -1):
            if inFile[i]==".":
                ext=inFile[i:]
                break

        f = open(inFile, 'rb')
        s = f.read()
        s = bytearray(s)
        f.close()
        m = 256
        sum = len(s)
        a = Entry3.get()
        c = Entry4.get()
        arr = [0] * sum
        arr[0] = Entry5.get()
        if (not a.isdigit()) or (int(a) < 0) or(not c.isdigit()) or (int(c) < 0) or(not arr[0].isdigit()) or (int(arr[0])<0):
            messagebox.showerror('Ошибка', 'Неверный параметр.')
        else:
            arr[0] = int(arr[0])
            a = int(a)
            c = int(c)
            for i in range(sum - 1):
                arr[i + 1] = (a * arr[i] + c) % m

            for i in range(len(s)):
                s[i] = s[i] ^ arr[i]
            outFile = fd.asksaveasfilename()
            outFile+=ext
            fo = open(outFile, 'wb')
            fo.write(s)
            fo.close()
            Entry2.delete(0, END)
            Entry2.insert(0, outFile)
            Entry2.insert(0, "Cохранено: ")

    def encode(s):
        return list(map(lambda x: "{0:b}".format(ord(x)).zfill(16), s))

    def decode(lst):
        return ''.join(map(lambda x: chr(int(x, 2)), lst))

    def keyCr(a, c, arr0):
        openSTR = Text1.get(1.0, END)
        openSTR=openSTR[:-1]

        keyBin = [[0] * 16 for i in range(len(openSTR))]
        m = 65536
        sum = len(openSTR)
        arr = [0] * sum
        arr[0] = arr0
        if 0:
            messagebox.showerror('Ошибка', 'Неверный параметр.')
        else:
            for i in range(sum - 1):
                arr[i + 1] = (a * arr[i] + c) % m

        for i in range(len(openSTR)):
            a=arr[i]
            for j in range(15, 0, -1):
                if a != 0:
                    if a % 2 == 0:
                        keyBin[i][j]=0
                        a = a // 2
                    elif a % 2:
                        keyBin[i][j]=1
                        a = a // 2
                else:
                    break
        for i in range(len(openSTR)):
            keyBin[i] = "".join(map(str, keyBin[i]))
        key = decode(keyBin)
        return key

    def rishE():
        openSTRT = Text1.get(1.0, END)
        openSTRT = openSTRT[:-1]
        a = Entry3.get()
        c = Entry4.get()
        arr0= Entry5.get()

        if (not a.isdigit()) or (int(a) < 0) or (not c.isdigit()) or (int(c) < 0) or (not arr0.isdigit()) or (
                int(arr0) < 0):
            messagebox.showerror('Ошибка', 'Неверный параметр.')
        else:
            arr0 = int(arr0)
            a = int(a)
            c = int(c)
            openSTRbin = encode(openSTRT)
            key=keyCr(a, c, arr0)
            keyBin = encode(key)
            cipherSTRbin = [[0] * 16 for i in range(len(openSTRbin))]
            for i in range(len(openSTRbin)):
                for j in range(16):
                    cipherSTRbin[i][j] = int(openSTRbin[i][j]) ^ int(keyBin[i][j])
            for i in range(len(openSTRbin)):
                cipherSTRbin[i] = "".join(map(str, cipherSTRbin[i]))
            cipherSTR = decode(cipherSTRbin)
            if not cipherSTR.isprintable():
                messagebox.showerror('Ошибка', 'Ошибка зашифрования, введите другой ключ.')
            else:
                Text2.delete(1.0, END)
                Text2.insert(1.0, cipherSTR)

    gammaW = Tk()
    gammaW.geometry("600x287+405+256")
    gammaW.minsize(120, 1)
    gammaW.maxsize(1444, 941)
    gammaW.resizable(1, 1)
    gammaW.title("Toplevel 0")
    gammaW.configure(background="#e6fdff")

    Label1 = Label(gammaW)
    Label1.place(relx=0.383, rely=0.0, height=33, width=144)
    Label1.configure(anchor='w')
    Label1.configure(background="#e6fdff")
    Label1.configure(compound='left')
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(font="-family {Times New Roman} -size 14 -weight bold")
    Label1.configure(foreground="#000000")
    Label1.configure(text='''Гаммирование''')

    openB = Button(gammaW, command=openF)
    openB.place(relx=0.7, rely=0.105, height=24, width=167)
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

    Entry1 = Entry(gammaW)
    Entry1.place(relx=0.033, rely=0.105, height=30, relwidth=0.64)
    Entry1.configure(background="white")
    Entry1.configure(disabledforeground="#a3a3a3")
    Entry1.configure(font="-family {Courier New} -size 12")
    Entry1.configure(foreground="#000000")
    Entry1.configure(insertbackground="black")

    Entry2 = Entry(gammaW)
    Entry2.place(relx=0.033, rely=0.244, height=30, relwidth=0.64)
    Entry2.configure(background="white")
    Entry2.configure(disabledforeground="#a3a3a3")
    Entry2.configure(font="-family {Courier New} -size 12")
    Entry2.configure(foreground="#000000")
    Entry2.configure(insertbackground="black")

    saveB = Button(gammaW, command=saveF)
    saveB.place(relx=0.7, rely=0.244, height=24, width=167)
    saveB.configure(activebackground="beige")
    saveB.configure(activeforeground="#000000")
    saveB.configure(background="#e9e9e9")
    saveB.configure(compound='left')
    saveB.configure(disabledforeground="#a3a3a3")
    saveB.configure(foreground="#000000")
    saveB.configure(highlightbackground="#d9d9d9")
    saveB.configure(highlightcolor="black")
    saveB.configure(pady="0")
    saveB.configure(text='''Зашифровать и сохранить''')

    Entry3 = Entry(gammaW)
    Entry3.place(relx=0.033, rely=0.383, height=30, relwidth=0.14)
    Entry3.configure(background="white")
    Entry3.configure(disabledforeground="#a3a3a3")
    Entry3.configure(font="-family {Courier New} -size 12")
    Entry3.configure(foreground="#000000")
    Entry3.configure(insertbackground="black")
    Entry3.insert(0, "2347")

    Entry4 = Entry(gammaW)
    Entry4.place(relx=0.317, rely=0.383, height=30, relwidth=0.14)
    Entry4.configure(background="white")
    Entry4.configure(disabledforeground="#a3a3a3")
    Entry4.configure(font="-family {Courier New} -size 12")
    Entry4.configure(foreground="#000000")
    Entry4.configure(insertbackground="black")
    Entry4.insert(0, "1283")

    Entry5 = Entry(gammaW)
    Entry5.place(relx=0.617, rely=0.383, height=30, relwidth=0.14)
    Entry5.configure(background="white")
    Entry5.configure(disabledforeground="#a3a3a3")
    Entry5.configure(font="-family {Courier New} -size 12")
    Entry5.configure(foreground="#000000")
    Entry5.configure(insertbackground="black")
    Entry5.insert(0, "0")

    Label2 = Label(gammaW)
    Label2.place(relx=0.183, rely=0.383, height=21, width=74)
    Label2.configure(anchor='w')
    Label2.configure(background="#e6fdff")
    Label2.configure(compound='left')
    Label2.configure(disabledforeground="#a3a3a3")
    Label2.configure(foreground="#000000")
    Label2.configure(text='''Множитель''')

    Label3 = Label(gammaW)
    Label3.place(relx=0.467, rely=0.383, height=21, width=84)
    Label3.configure(anchor='w')
    Label3.configure(background="#e6fdff")
    Label3.configure(compound='left')
    Label3.configure(disabledforeground="#a3a3a3")
    Label3.configure(foreground="#000000")
    Label3.configure(text='''Приращение''')

    Label4 = Label(gammaW)
    Label4.place(relx=0.767, rely=0.383, height=21, width=134)
    Label4.configure(anchor='w')
    Label4.configure(background="#e6fdff")
    Label4.configure(compound='left')
    Label4.configure(disabledforeground="#a3a3a3")
    Label4.configure(foreground="#000000")
    Label4.configure(text='''Начальное значение''')

    Text1 = Text(gammaW)
    Text1.place(relx=0.033, rely=0.523, relheight=0.432, relwidth=0.373)

    Text1.configure(background="white")
    Text1.configure(font="TkTextFont")
    Text1.configure(foreground="black")
    Text1.configure(highlightbackground="#d9d9d9")
    Text1.configure(highlightcolor="black")
    Text1.configure(insertbackground="black")
    Text1.configure(selectbackground="#c4c4c4")
    Text1.configure(selectforeground="black")
    Text1.configure(wrap="word")

    Text2 = Text(gammaW)
    Text2.place(relx=0.6, rely=0.523, relheight=0.432, relwidth=0.373)
    Text2.configure(background="white")
    Text2.configure(font="TkTextFont")
    Text2.configure(foreground="black")
    Text2.configure(highlightbackground="#d9d9d9")
    Text2.configure(highlightcolor="black")
    Text2.configure(insertbackground="black")
    Text2.configure(selectbackground="#c4c4c4")
    Text2.configure(selectforeground="black")
    Text2.configure(wrap="word")

    textEB = Button(gammaW, command=rishE)
    textEB.place(relx=0.433, rely=0.662, height=24, width=87)
    textEB.configure(activebackground="beige")
    textEB.configure(activeforeground="#000000")
    textEB.configure(background="#d9d9d9")
    textEB.configure(compound='left')
    textEB.configure(disabledforeground="#a3a3a3")
    textEB.configure(foreground="#000000")
    textEB.configure(highlightbackground="#d9d9d9")
    textEB.configure(highlightcolor="black")
    textEB.configure(pady="0")
    textEB.configure(text='''Зашифровать''')

    gammaW.mainloop()