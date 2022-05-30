from tkinter import *
from AtbashCode import *
from tkinter import messagebox
def atbash():

    def clickedE():
        openSTR = openText.get(1.0, END)
        cipherSTR=""
        for i in range(len(openSTR)-1):
            check = 1
            for j in range(len(atbashCode[0])):
                if openSTR[i]==atbashCode[0][j]:
                    cipherSTR=cipherSTR+atbashCode[1][j]
                    check=0
            if check==1:
                cipherSTR = cipherSTR + openSTR[i]
        cipherText.delete(1.0, END)
        cipherText.insert(1.0, cipherSTR)

    def clickedD():
        openSTR = cipherText.get(1.0, END)
        cipherSTR=""
        for i in range(len(openSTR)):
            check = 1
            for j in range(len(atbashCode[0])):
                if openSTR[i]==atbashCode[0][j]:
                    cipherSTR=cipherSTR+atbashCode[1][j]
                    check=0
            if check==1:
                cipherSTR = cipherSTR + openSTR[i]
        openText.delete(1.0, END)
        openText.insert(1.0, cipherSTR)

    def clickedI():
        messagebox.showinfo('Об Атбаш', 'Атба́ш  — простой шифр подстановки для алфавитного письма.'
                                        'Правило шифрования Атбаш состоит в замене n-й буквы алфавита буквой '
                                        'с номером m − n + 1, где m — число букв в алфавите. '
                                        'Таким образом алгоритм зашифровки и расшифровки идентичны')

    atbashW = Tk()
    atbashW.geometry("716x263+322+179")
    atbashW.title("Атбаш")
    atbashW.configure(background="#ffcece")

    openText = Text(atbashW)
    openText.place(relx=0.029, rely=0.3, relheight=0.612, relwidth=0.37)
    openText.configure(background="white")
    openText.configure(borderwidth="2")
    openText.configure(font="-family {@Malgun Gothic} -size 13")
    openText.configure(foreground="black")

    cipherText = Text(atbashW)
    cipherText.place(relx=0.601, rely=0.3, relheight=0.612, relwidth=0.37)
    cipherText.configure(background="white")
    cipherText.configure(borderwidth="2")
    cipherText.configure(font="-family {@Malgun Gothic} -size 13")
    cipherText.configure(foreground="black")


    encryptAtbash = Button(atbashW, command=clickedE)
    encryptAtbash.place(relx=0.42, rely=0.418, height=34, width=114)
    encryptAtbash.configure(background="#ffffff")
    encryptAtbash.configure(borderwidth="3")
    encryptAtbash.configure(cursor="hand2")
    encryptAtbash.configure(font="-family {@Malgun Gothic} -size 10")
    encryptAtbash.configure(foreground="#000000")
    encryptAtbash.configure(text='''Зашифровать ->''')

    decipherAtbash = Button(atbashW, command=clickedD)
    decipherAtbash.place(relx=0.42, rely=0.608, height=34, width=114)
    decipherAtbash.configure(background="#ffffff")
    decipherAtbash.configure(borderwidth="3")
    decipherAtbash.configure(cursor="hand2")
    decipherAtbash.configure(font="-family {@Malgun Gothic} -size 10")
    decipherAtbash.configure(foreground="#000000")
    decipherAtbash.configure(text='''<-Расшифровать''')

    headAtbash = Label(atbashW)
    headAtbash.place(relx=0.377, rely=0.076, height=51, width=191)
    headAtbash.configure(background="#ffcece")
    headAtbash.configure(font="-family {Open Sans Light} -size 20 -weight bold")
    headAtbash.configure(foreground="#000000")
    headAtbash.configure(text='''Шифр Атбаш''')

    information = Button(atbashW, command=clickedI)
    information.place(relx=0.95, rely=0.038, height=24, width=27)
    information.configure(background="#ffffff")
    information.configure(borderwidth="3")
    information.configure(compound='left')
    information.configure(cursor="question_arrow")
    information.configure(font="-family {Segoe UI} -size 11")
    information.configure(foreground="#000000")
    information.configure(text='''?''')

    atbashW.mainloop()






