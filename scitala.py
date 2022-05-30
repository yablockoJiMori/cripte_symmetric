from tkinter import *

from tkinter import messagebox
def scitala():

    def scitalaE():
        openSTR = openText.get(1.0, END)
        keyN = keyScitala.get()
        char = charScitala.get()
        if keyN.isdigit():
            if len(char) == 0 or len(char) > 1:
                messagebox.showerror('Ошибка', 'Введите один символ.')
                return 0
            else:
                if char==openSTR[len(openSTR)-2]:
                    res = messagebox.askquestion('Предупреждение', 'Заполняющий символ совпадает с последний символом введенного сообщения. '
                                                              'При расшифровки этот символ будет утерян. Продолжить?')
                    if res == 0:
                        return 0
                keyN=int(keyN)
                keyM = (len(openSTR)-2)//int(keyN)+1
                cipherSTR=""
                for i in range(keyM):
                    for j in range(keyN):
                        if (keyM*j+i+1) < len(openSTR):
                            cipherSTR=cipherSTR+openSTR[keyM*j+i]
                        else:
                            cipherSTR = cipherSTR + char
        else:
            messagebox.showerror('Ошибка', 'Некорректный ключ. Введите число.')
            return 0
        cipherText.delete(1.0, END)
        cipherText.insert(1.0, cipherSTR)

    def scitalaD():
        openSTR = cipherText.get(1.0, END)
        char = charScitala.get()
        keyN = keyScitala.get()
        if keyN.isdigit():
            keyN = int(keyN)
            keyM = (len(openSTR) - 2) // int(keyN) + 1
            cipherSTR=""
            for j in range(keyN):
                for i in range(keyM):
                    cipherSTR = cipherSTR + openSTR[keyN * i + j]
        else:
            messagebox.showerror('Ошибка', 'Некорректный ключ. Введите число.')
        openText.delete(1.0, END)
        openText.insert(1.0, cipherSTR.rstrip(char))

    def scitalaI():
        messagebox.showinfo('Об Сцитала', 'Скита́ла или сцита́ла  — инструмент, используемый для осуществления '
                                          'перестановочного шифрования, в криптографии известный также как шифр'
                                          ' Древней Спарты. Представляет собой цилиндр и узкую полоску пергамента, '
                                          'на которой писалось сообщение, обматывавшуюся вокруг него по спирали.'
                                          'В результате шифрования получается таблица, у которой есть два параметра: '
                                          'n — количество строк, m — количество столбцов. В качестве ключа используется n.')

    scitalaW = Tk()
    scitalaW.geometry("716x263+322+179")
    scitalaW.title("Сцитала")
    scitalaW.configure(background="#ffcece")

    openText = Text(scitalaW)
    openText.place(relx=0.029, rely=0.3, relheight=0.612, relwidth=0.37)
    openText.configure(background="white")
    openText.configure(borderwidth="2")
    openText.configure(font="-family {@Malgun Gothic} -size 13")
    openText.configure(foreground="black")

    cipherText = Text(scitalaW)
    cipherText.place(relx=0.601, rely=0.3, relheight=0.612, relwidth=0.37)
    cipherText.configure(background="white")
    cipherText.configure(borderwidth="2")
    cipherText.configure(font="-family {@Malgun Gothic} -size 13")
    cipherText.configure(foreground="black")

    encryptAtbash = Button(scitalaW, command=scitalaE)
    encryptAtbash.place(relx=0.419, rely=0.305, height=34, width=115)
    encryptAtbash.configure(background="#ffffff")
    encryptAtbash.configure(borderwidth="3")
    encryptAtbash.configure(cursor="hand2")
    encryptAtbash.configure(font="-family {@Malgun Gothic} -size 10")
    encryptAtbash.configure(foreground="#000000")
    encryptAtbash.configure(text='''Зашифровать ->''')

    decipherAtbash = Button(scitalaW, command=scitalaD)
    decipherAtbash.place(relx=0.419, rely=0.455, height=34, width=114)
    decipherAtbash.configure(background="#ffffff")
    decipherAtbash.configure(borderwidth="3")
    decipherAtbash.configure(cursor="hand2")
    decipherAtbash.configure(font="-family {@Malgun Gothic} -size 10")
    decipherAtbash.configure(foreground="#000000")
    decipherAtbash.configure(text='''<-Расшифровать''')

    headScitala = Label(scitalaW)
    headScitala.place(relx=0.363, rely=0.075, height=52, width=201)
    headScitala.configure(background="#ffcece")
    headScitala.configure(font="-family {Open Sans Light} -size 20 -weight bold")
    headScitala.configure(foreground="#000000")
    headScitala.configure(text='''Шифр Сцитала''')

    information = Button(scitalaW, command=scitalaI)
    information.place(relx=0.95, rely=0.038, height=24, width=27)
    information.configure(background="#ffffff")
    information.configure(borderwidth="3")
    information.configure(compound='left')
    information.configure(cursor="question_arrow")
    information.configure(font="-family {Segoe UI} -size 11")
    information.configure(foreground="#000000")
    information.configure(text='''?''')

    keyScitala = Entry(scitalaW)
    keyScitala.place(relx=0.419, rely=0.602, height=30, relwidth=0.159)
    keyScitala.configure(background="white")
    keyScitala.configure(borderwidth="2")
    keyScitala.configure(font="-family {@Malgun Gothic} -size 14")
    keyScitala.configure(foreground="#000000")

    headKey = Label(scitalaW)
    headKey.place(relx=0.466, rely=0.714, height=11, width=43)
    headKey.configure(background="#ffcece")
    headKey.configure(font="-family {@Malgun Gothic} -size 8")
    headKey.configure(foreground="#000000")
    headKey.configure(text='''Ключ''')

    headChar = Label(scitalaW)
    headChar.place(relx=0.412, rely=0.865, height=21, width=134)
    headChar.configure(background="#ffcece")
    headChar.configure(disabledforeground="#a3a3a3")
    headChar.configure(font="-family {@Malgun Gothic} -size 8")
    headChar.configure(foreground="#000000")
    headChar.configure(text='''Заполняющий символ''')

    charScitala = Entry(scitalaW)
    charScitala.place(relx=0.419, rely=0.771, height=30, relwidth=0.159)
    charScitala.configure(background="white")
    charScitala.configure(borderwidth="2")
    charScitala.configure(font="-family {@Malgun Gothic} -size 14")
    charScitala.configure(foreground="#000000")

    scitalaW.mainloop()