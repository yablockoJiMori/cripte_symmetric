from tkinter import *
from tkinter.constants import *
from tkinter import messagebox
from tkinter import filedialog as fd
def caesar():
    alphabetRUSup = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alphabetRUSlo = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabetENGup = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabetENGlo = 'abcdefghijklmnopqrstuvwxyz'

    def caesarE():
        openSTR = openText.get(1.0, END)
        key = keyCaesar.get()
        if not key.isdigit():
            messagebox.showerror('Ошибка', 'Неверный сдвиг.')
        else:
            n = int(key)
            cipherSTR = ""
            for i in range(len(openSTR)-1):
                for j in range(len(alphabetRUSup)):
                    if openSTR[i] == alphabetRUSup[j]:
                        cipherSTR = cipherSTR + alphabetRUSup[(j + n) % 33]
                for j in range(len(alphabetRUSlo)):
                    if openSTR[i] == alphabetRUSlo[j]:
                        cipherSTR = cipherSTR + alphabetRUSlo[(j + n) % 33]
                for j in range(len(alphabetENGup)):
                    if openSTR[i] == alphabetENGup[j]:
                        cipherSTR = cipherSTR + alphabetENGup[(j + n) % 26]
                for j in range(len(alphabetENGlo)):
                    if openSTR[i] == alphabetENGlo[j]:
                        cipherSTR = cipherSTR + alphabetENGlo[(j + n) % 26]
                if not openSTR[i].isalpha():
                    cipherSTR = cipherSTR + openSTR[i]
            cipherText.delete(1.0, END)
            cipherText.insert(1.0, cipherSTR)

    def caesarD():
        openSTR = cipherText.get(1.0, END)
        key = keyCaesar.get()
        n = int(key)
        if not key.isdigit():
            messagebox.showerror('Ошибка', 'Неверный сдвиг.')
        else:
            cipherSTR = ""
            for i in range(len(openSTR)-1):
                for j in range(len(alphabetRUSup)):
                    if openSTR[i] == alphabetRUSup[j]:
                        cipherSTR = cipherSTR + alphabetRUSup[(j - n) % 33]
                for j in range(len(alphabetRUSlo)):
                    if openSTR[i] == alphabetRUSlo[j]:
                        cipherSTR = cipherSTR + alphabetRUSlo[(j - n) % 33]
                for j in range(len(alphabetENGup)):
                    if openSTR[i] == alphabetENGup[j]:
                        cipherSTR = cipherSTR + alphabetENGup[(j - n) % 26]
                for j in range(len(alphabetENGlo)):
                    if openSTR[i] == alphabetENGlo[j]:
                        cipherSTR = cipherSTR + alphabetENGlo[(j - n) % 26]
                if not openSTR[i].isalpha():
                    cipherSTR = cipherSTR + openSTR[i]
            openText.delete(1.0, END)
            openText.insert(1.0, cipherSTR)

    def caesarI():
        messagebox.showinfo('О шифре Цезаря', 'Шифр Цезаря, также известный как шифр сдвига, '
                                              'код Цезаря или сдвиг Цезаря — один из самых простых '
                                              'и наиболее широко известных методов шифрования. Шифр '
                                              'Цезаря — это вид шифра подстановки, в котором каждый '
                                              'символ в открытом тексте заменяется символом, '
                                              'находящимся на некотором постоянном числе позиций '
                                              'левее или правее него в алфавите. Например, в шифре со '
                                              'сдвигом вправо на 3, А была бы заменена на Г, Б станет Д, и так далее.')

    def openF():
        inFile = fd.askopenfilename()
        f = open(inFile)
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

    caesarW = Tk()
    caesarW.geometry("716x263+322+179")
    caesarW.title("Цезарь")
    caesarW.configure(background="#ffcece")

    openText = Text(caesarW)
    openText.place(relx=0.029, rely=0.3, relheight=0.612, relwidth=0.37)
    openText.configure(background="white")
    openText.configure(borderwidth="2")
    openText.configure(font="-family {@Malgun Gothic} -size 13")
    openText.configure(foreground="black")

    cipherText = Text(caesarW)
    cipherText.place(relx=0.601, rely=0.3, relheight=0.612, relwidth=0.37)
    cipherText.configure(background="white")
    cipherText.configure(borderwidth="2")
    cipherText.configure(font="-family {@Malgun Gothic} -size 13")
    cipherText.configure(foreground="black")

    encryptCaesar = Button(caesarW, command=caesarE)
    encryptCaesar.place(relx=0.419, rely=0.305, height=34, width=115)
    encryptCaesar.configure(background="#ffffff")
    encryptCaesar.configure(borderwidth="3")
    encryptCaesar.configure(cursor="hand2")
    encryptCaesar.configure(font="-family {@Malgun Gothic} -size 10")
    encryptCaesar.configure(foreground="#000000")
    encryptCaesar.configure(text='''Зашифровать ->''')

    decipherCaesar = Button(caesarW, command=caesarD)
    decipherCaesar.place(relx=0.419, rely=0.455, height=34, width=114)
    decipherCaesar.configure(background="#ffffff")
    decipherCaesar.configure(borderwidth="3")
    decipherCaesar.configure(cursor="hand2")
    decipherCaesar.configure(font="-family {@Malgun Gothic} -size 10")
    decipherCaesar.configure(foreground="#000000")
    decipherCaesar.configure(text='''<-Расшифровать''')

    headCaesar = Label(caesarW)
    headCaesar.place(relx=0.279, rely=0.075, height=52, width=341)
    headCaesar.configure(background="#ffcece")
    headCaesar.configure(font="-family {Open Sans Light} -size 20 -weight bold")
    headCaesar.configure(foreground="#000000")
    headCaesar.configure(text='''Шифр Цезаря''')

    information = Button(caesarW, command=caesarI)
    information.place(relx=0.95, rely=0.038, height=24, width=27)
    information.configure(background="#ffffff")
    information.configure(borderwidth="3")
    information.configure(compound='left')
    information.configure(cursor="question_arrow")
    information.configure(font="-family {Segoe UI} -size 11")
    information.configure(foreground="#000000")
    information.configure(text='''?''')

    headChar = Label(caesarW)
    headChar.place(relx=0.412, rely=0.865, height=21, width=134)
    headChar.configure(background="#ffcece")
    headChar.configure(disabledforeground="#a3a3a3")
    headChar.configure(font="-family {@Malgun Gothic} -size 8")
    headChar.configure(foreground="#000000")
    headChar.configure(text='''Ключ''')

    keyCaesar = Entry(caesarW)
    keyCaesar.place(relx=0.419, rely=0.771, height=30, relwidth=0.159)
    keyCaesar.configure(background="white")
    keyCaesar.configure(borderwidth="2")
    keyCaesar.configure(font="-family {@Malgun Gothic} -size 14")
    keyCaesar.configure(foreground="#000000")

    openF = Button(caesarW, command=openF)
    openF.place(relx=0.028, rely=0.15, height=24, width=147)
    openF.configure(background="#ffffff")
    openF.configure(borderwidth="3")
    openF.configure(compound='left')
    openF.configure(cursor="hand2")
    openF.configure(font="-family {@Malgun Gothic} -size 10")
    openF.configure(text='''Открыть файл''')

    saveF = Button(caesarW, command=saveF)
    saveF.place(relx=0.768, rely=0.15, height=24, width=147)
    saveF.configure(background="#ffffff")
    saveF.configure(borderwidth="3")
    saveF.configure(compound='left')
    saveF.configure(cursor="hand2")
    saveF.configure(font="-family {@Malgun Gothic} -size 10")
    saveF.configure(text='''Сохранить в файл''')

    caesarW.mainloop()