from tkinter import *
from tkinter.constants import *
from tkinter import messagebox
from tkinter import filedialog as fd
from const import *
import tkinter.ttk as ttk
from random import randbytes
def DESf():
    def openKey():
        inFile = fd.askopenfilename()
        try:
            f = open(inFile, encoding="utf-8")
            s = f.read()
            keyE.delete(0, END)
            keyE.insert(0, s)
            f.close()
        except Exception as e:
            print(e)
            messagebox.showerror('Ошибка', e)

    def openIV():
        inFile = fd.askopenfilename()
        try:
            f = open(inFile, encoding="utf-8")
            s = f.read()
            ivE.delete(0, END)
            ivE.insert(0, s)
            f.close()
        except Exception as e:
            print(e)
            messagebox.showerror('Ошибка', e)

    def saveKey():
        outFile = fd.asksaveasfilename()
        outFile += ".txt"
        f = open(outFile, 'w', encoding="utf-8")
        s = keyE.get()
        f.write(s)
        f.close()

    def saveIV():
        outFile = fd.asksaveasfilename()
        outFile += ".txt"
        f = open(outFile, 'w', encoding="utf-8")
        s = ivE.get()
        f.write(s)
        f.close()

    def openF():
        inFile = fd.askopenfilename()
        fileINE.delete(0, END)
        fileINE.insert(0, inFile)

    def ButEnc():
        modeDES = TCombobox1.get()
        openKey = keyE.get()
        keys = genKeys(openKey)
        if type(keys)!=int:
            fileIN = fileINE.get()

            #Сохраняем формат
            ext=""
            for i in range(len(fileIN) - 1, 0, -1):
                if fileIN[i] == ".":
                    ext = fileIN[i:]
                    break


            fileOUT = fd.asksaveasfilename()
            fileOUT += ext
            fileOUTE.delete(0, END)
            fileOUTE.insert(0, fileOUT)
            try:
                with open(fileIN, "rb") as fileIN, \
                        open(fileOUT, "wb") as fileOUT:
                    fileIN.seek(0, 2)
                    fileIN_size = fileIN.tell()
                    fileIN.seek(0, 0)

                    #сохраняем размер
                    pad = fileIN_size.to_bytes(8, "little")
                    if (k := len(pad) % 8) != 0:
                        pad += b"\00" * (8 - k)
                    fileOUT.write(pad)

                    openSTR = fileIN.read()
                    openSTR = bytearray(openSTR)
                    match modeDES:
                        case "ECB":
                            openSTR = ECB(keys, openSTR, mode="encrypt")
                        case "CBC":
                            openSTR = CBC(keys, openSTR, mode="encrypt")
                        case "CFB":
                            openSTR = CFB(keys, openSTR, mode="encrypt")
                        case "OFB":
                            openSTR = OFB(keys, openSTR, mode="encrypt")
                        case _:
                            print(f"Нет такого режима! -> {modeDES}")
                            return 0

                    fileOUT.write(openSTR)

            except Exception as e:
                print(e)
                messagebox.showerror('Ошибка', e)

    def ButDec():
        modeDES = TCombobox1.get()
        openKey = keyE.get()
        keys = genKeys(openKey)
        fileIN = fileINE.get()

        #сохраняем формат
        ext = ""
        for i in range(len(fileIN) - 1, 0, -1):
            if fileIN[i] == ".":
                ext = fileIN[i:]
                break
        fileOUT = fd.asksaveasfilename()
        fileOUT += ext
        fileOUTE.delete(0, END)
        fileOUTE.insert(0, fileOUT)

        try:
            with open(fileIN, "rb") as fileIN, \
                    open(fileOUT, "wb") as fileOUT:

                #считываем размер
                pad = fileIN.read(8)
                final_file_size = int.from_bytes(pad, "little")

                openSTR = fileIN.read()
                openSTR = bytearray(openSTR)
                match modeDES:
                    case "ECB":
                        openSTR = ECB(keys, openSTR, mode="decrypt")
                    case "CBC":
                        openSTR = CBC(keys, openSTR, mode="decrypt")
                    case "CFB":
                        openSTR = CFB(keys, openSTR, mode="decrypt")
                    case "OFB":
                        openSTR = OFB(keys, openSTR, mode="decrypt")
                    case _:
                        print(f"Нет такого режима! -> {modeDES}")
                        return 0
                fileOUT.write(openSTR)
                #ровняем до нужного размера
                fileOUT.truncate(final_file_size)

        except Exception as e:
           print(e)
           messagebox.showerror('Ошибка', e)

    def RandomKey():
        key=randbytes(7).decode("koi8-r")
        keyE.delete(0, END)
        keyE.insert(0, key)

    def RandomIV():
        iv=randbytes(8).decode("koi8-r")
        ivE.delete(0, END)
        ivE.insert(0, iv)

    def genKeys(key):
        if len(key.encode("koi8-r")) != 7:
            fl=len(key.encode("koi8-r"))
            messagebox.showerror('Ошибка', f"Длина ключа должна быть 56 бит (7 байт)! ({fl} байт введено)")
            return 0


        key = key.encode("koi8-r")
        key = int.from_bytes(key, "little")

        new_key = 0

        # Getting a 64-bit key
        for i in range(8):
            k = (key >> (i * 7)) & 0b1111111

            match bin(k).count("1") % 2:
                case 0:
                    new_key |= ((k << 1) | 0b1) << (8 * i)

                case 1:
                    new_key |= ((k << 1) | 0b0) << (8 * i)
        #перемешивание без учета добавленных битов
        new_key = permut(new_key, 64, DES_PC_1_TABLE)


        key_C = new_key >> 28
        key_D = new_key & 0xFFFFFFF
        keys = []

        for i in range(16):
            shift = DES_SHIFT_TABLE[i]

            key_C = ((key_C << shift) | (key_C >> (28 - shift))) & 0xFFFFFFF
            key_D = ((key_D << shift) | (key_D >> (28 - shift))) & 0xFFFFFFF

            new_key = (key_C << 28) | key_D
            #перестановка с уменьшением до 48 бит
            new_key = permut(new_key, 56, DES_PC_2_TABLE)
            keys.append(new_key)

        return keys

    def genIV(iv):
        if len(iv.encode("koi8-r")) != 8:
            fl=len(iv.encode("koi8-r"))
            messagebox.showerror('Ошибка', f"Длина начального вектора должна быть 64 бит (8 байт)! ({fl} байт введено)")
            return 0

        iv = iv.encode("koi8-r")
        iv = int.from_bytes(iv, "little")
        return iv

    def permut(block: int, bit_len: int, table: tuple):
        block = bin(block)[2:].zfill(bit_len)
        return int("".join(block[i - 1] for i in table), 2)

    def transform(keys, block: int, mode: str = "encrypt"):
        block = permut(block, 64, DES_IP_TABLE)

        block_L = block >> 32
        block_R = block & 0xFFFFFFFF


        match mode:
            case "encrypt":
                for i in range(16):
                    block_L, block_R = block_R, block_L ^ f(block_R, keys[i])

            case "decrypt":
                for i in range(15, -1, -1):
                    block_R, block_L = block_L, block_R ^ f(block_L, keys[i])

            case _:
                print(f"Invalid processing mode! -> {mode}")
                return 0

        block = (block_L << 32) | block_R
        return permut(block, 64, DES_IP_INV_TABLE)

    def f(block: int, key: int):
        #расширяем до 48 бит
        block = permut(block, 32, DES_E_TABLE) ^ key

        new_block = 0
        for k in range(8):
            b = block >> (6 * k) & 0b111111
            i = ((b >> 5) << 1) | (b & 0b1)
            j = (b >> 1) & 0b1111
            new_block |= DES_S_TABLE[7 - k][i][j] << (6 * k)
        #уменьшая до 32
        return permut(new_block, 48, DES_P_TABLE)

    def ECB(keys, data: bytes, mode: str = "encrypt"):
        master = Tk()
        master.geometry("608x40+390+572")
        master.configure(background="#e6fdff")
        progress_bar = ttk.Progressbar(master, orient="horizontal", mode="determinate", value=0)
        progress_bar.place(relx=0.016, rely=0.25, relwidth=0.969, relheight=0.0, height=22)
        progress_bar.configure(length="589")
        progress_bar.configure(maximum=(len(data)//8))
        master.update()
        progress_bar['value'] = 0
        master.update()

        processed_data = bytes()

        for pos in range(0, len(data), 8):
            block = int.from_bytes(data[pos:pos + 8], "little")
            processed_block = transform(keys, block, mode)
            progress_bar['value'] += 1
            master.update()
            processed_data += processed_block.to_bytes(8, "little")

        master.destroy()
        return processed_data

    def CBC(keys, data: bytes, mode: str = "encrypt"):

        iv = ivE.get()
        iv = genIV(iv)
        if iv != 0:
            master = Tk()
            master.geometry("608x40+390+572")
            master.configure(background="#e6fdff")
            progress_bar = ttk.Progressbar(master, orient="horizontal", mode="determinate", value=0)
            progress_bar.place(relx=0.016, rely=0.25, relwidth=0.969, relheight=0.0, height=22)
            progress_bar.configure(length="589")
            progress_bar.configure(maximum=(len(data) // 8))
            master.update()
            progress_bar['value'] = 0
            master.update()

            vector = iv
            processed_data = bytes()
            for pos in range(0, len(data), 8):
                block = int.from_bytes(data[pos:pos + 8], "little")

                match mode:
                    case "encrypt":
                        processed_block = transform(keys, block ^ vector, "encrypt")
                        vector = processed_block
                        progress_bar['value'] += 1
                        master.update()

                    case "decrypt":
                        processed_block = transform(keys, block, "decrypt") ^ vector
                        vector = block
                        progress_bar['value'] += 1
                        master.update()

                    case _:
                        print(f"Invalid processing mode! -> {mode}")
                        return 0
                processed_data += processed_block.to_bytes(8, "little")
            master.destroy()
            return processed_data

    def CFB(keys, data: bytes, mode: str = "encrypt"):
        master = Tk()
        master.geometry("608x40+390+572")
        master.configure(background="#e6fdff")
        progress_bar = ttk.Progressbar(master, orient="horizontal", mode="determinate", value=0)
        progress_bar.place(relx=0.016, rely=0.25, relwidth=0.969, relheight=0.0, height=22)
        progress_bar.configure(length="589")
        progress_bar.configure(maximum=(len(data) // 8))
        master.update()
        progress_bar['value'] = 0
        master.update()
        iv = ivE.get()
        iv = genIV(iv)
        processed_data = bytes()
        vector = iv

        for pos in range(0, len(data), 8):
            block = int.from_bytes(data[pos:pos + 8], "little")

            match mode:
                case "encrypt":
                    processed_block = transform(keys, vector, "encrypt") ^ block
                    progress_bar['value'] += 1
                    master.update()
                    vector = processed_block

                case "decrypt":
                    processed_block = transform(keys, vector, "encrypt") ^ block
                    progress_bar['value'] += 1
                    master.update()
                    vector = block

                case _:
                    print(f"Invalid processing mode! -> {mode}")
                    return 0

            processed_data += processed_block.to_bytes(8, "little")
        master.destroy()
        return processed_data

    def OFB(keys, data: bytes, mode: str = "encrypt"):
        master = Tk()
        master.geometry("608x40+390+572")
        master.configure(background="#e6fdff")
        progress_bar = ttk.Progressbar(master, orient="horizontal", mode="determinate", value=0)
        progress_bar.place(relx=0.016, rely=0.25, relwidth=0.969, relheight=0.0, height=22)
        progress_bar.configure(length="589")
        progress_bar.configure(maximum=(len(data) // 8))
        master.update()
        progress_bar['value'] = 0
        master.update()
        iv = ivE.get()
        iv = genIV(iv)
        processed_data = bytes()
        vector = iv

        for pos in range(0, len(data), 8):
            block = int.from_bytes(data[pos:pos + 8], "little")

            match mode:
                case "encrypt":
                    vector = transform(keys, vector, "encrypt")
                    progress_bar['value'] += 1
                    master.update()
                    processed_block = vector ^ block

                case "decrypt":
                    vector = transform(keys, vector, "encrypt")
                    progress_bar['value'] += 1
                    master.update()
                    processed_block = vector ^ block

                case _:
                    print(f"Invalid processing mode! -> {mode}")
                    return 0

            processed_data += processed_block.to_bytes(8, "little")
        master.destroy()
        return processed_data


    desfW=Tk()
    desfW.geometry("600x295+393+238")
    desfW.minsize(120, 1)
    desfW.maxsize(1444, 941)
    desfW.resizable(1, 1)
    desfW.title("DES")
    desfW.configure(background="#e6fdff")


    Label1 = Label(desfW)
    Label1.place(relx=0.467, rely=0.034, height=20, width=44)
    Label1.configure(anchor='w')
    Label1.configure(background="#e6fdff")
    Label1.configure(compound='left')
    Label1.configure(cursor="fleur")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(font="-family {Courier New} -size 14")
    Label1.configure(foreground="#000000")
    Label1.configure(text='''DES''')

    fileINE = Entry(desfW)
    fileINE.place(relx=0.017, rely=0.136, height=30, relwidth=0.757)
    fileINE.configure(background="white")
    fileINE.configure(disabledforeground="#a3a3a3")
    fileINE.configure(font="TkFixedFont")
    fileINE.configure(foreground="#000000")
    fileINE.configure(insertbackground="black")

    openB = Button(desfW, command=openF)
    openB.place(relx=0.8, rely=0.136, height=24, width=107)
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

    keyE = Entry(desfW)
    keyE.place(relx=0.017, rely=0.373, height=30, relwidth=0.257)
    keyE.configure(background="white")
    keyE.configure(disabledforeground="#a3a3a3")
    keyE.configure(font="TkFixedFont")
    keyE.configure(foreground="#000000")
    keyE.configure(insertbackground="black")

    Label2 = Label(desfW)
    Label2.place(relx=0.017, rely=0.271, height=17, width=144)
    Label2.configure(anchor='w')
    Label2.configure(background="#e6fdff")
    Label2.configure(compound='left')
    Label2.configure(disabledforeground="#a3a3a3")
    Label2.configure(font="-family {Courier New} -size 12")
    Label2.configure(foreground="#000000")
    Label2.configure(text='''Ключ (56 бит)''')

    ivE = Entry(desfW)
    ivE.place(relx=0.533, rely=0.373, height=30, relwidth=0.257)
    ivE.configure(background="white")
    ivE.configure(disabledforeground="#a3a3a3")
    ivE.configure(font="TkFixedFont")
    ivE.configure(foreground="#000000")
    ivE.configure(insertbackground="black")

    Label2_1 = Label(desfW)
    Label2_1.place(relx=0.533, rely=0.271, height=24, width=284)
    Label2_1.configure(activebackground="#f9f9f9")
    Label2_1.configure(anchor='w')
    Label2_1.configure(background="#e6fdff")
    Label2_1.configure(compound='left')
    Label2_1.configure(disabledforeground="#a3a3a3")
    Label2_1.configure(font="-family {Courier New} -size 12")
    Label2_1.configure(foreground="#000000")
    Label2_1.configure(highlightbackground="#d9d9d9")
    Label2_1.configure(highlightcolor="black")
    Label2_1.configure(text='''Начальный вектор (64 бита)''')

    genKeyB = Button(desfW, command=RandomKey)
    genKeyB.place(relx=0.283, rely=0.339, height=24, width=107)
    genKeyB.configure(activebackground="beige")
    genKeyB.configure(activeforeground="#000000")
    genKeyB.configure(background="#e9e9e9")
    genKeyB.configure(compound='left')
    genKeyB.configure(disabledforeground="#a3a3a3")
    genKeyB.configure(foreground="#000000")
    genKeyB.configure(highlightbackground="#d9d9d9")
    genKeyB.configure(highlightcolor="black")
    genKeyB.configure(pady="0")
    genKeyB.configure(text='''Сгенерировать''')

    genIvB = Button(desfW, command=RandomIV)
    genIvB.place(relx=0.8, rely=0.339, height=24, width=107)
    genIvB.configure(activebackground="beige")
    genIvB.configure(activeforeground="#000000")
    genIvB.configure(background="#e9e9e9")
    genIvB.configure(compound='left')
    genIvB.configure(disabledforeground="#a3a3a3")
    genIvB.configure(foreground="#000000")
    genIvB.configure(highlightbackground="#d9d9d9")
    genIvB.configure(highlightcolor="black")
    genIvB.configure(pady="0")
    genIvB.configure(text='''Сгенерировать''')

    TCombobox1 = ttk.Combobox(desfW)
    TCombobox1.place(relx=0.017, rely=0.678, relheight=0.068
                , relwidth=0.255)
    TCombobox1.configure(takefocus="")
    TCombobox1['values'] = ("ECB", "CBC", "CFB", "OFB")
    TCombobox1.current(0)

    encB = Button(desfW, command=ButEnc)
    encB.place(relx=0.333, rely=0.712, height=34, width=97)
    encB.configure(activebackground="beige")
    encB.configure(activeforeground="#000000")
    encB.configure(background="#e9e9e9")
    encB.configure(compound='left')
    encB.configure(disabledforeground="#a3a3a3")
    encB.configure(foreground="#000000")
    encB.configure(highlightbackground="#d9d9d9")
    encB.configure(highlightcolor="black")
    encB.configure(pady="0")
    encB.configure(text='''Зашифровать''')

    decB = Button(desfW, command=ButDec)
    decB.place(relx=0.567, rely=0.712, height=34, width=97)
    decB.configure(activebackground="beige")
    decB.configure(activeforeground="#000000")
    decB.configure(background="#e9e9e9")
    decB.configure(compound='left')
    decB.configure(disabledforeground="#a3a3a3")
    decB.configure(foreground="#000000")
    decB.configure(highlightbackground="#d9d9d9")
    decB.configure(highlightcolor="black")
    decB.configure(pady="0")
    decB.configure(text='''Расшифровать''')

    Label2_2 = Label(desfW)
    Label2_2.place(relx=0.017, rely=0.576, height=27, width=144)
    Label2_2.configure(activebackground="#f9f9f9")
    Label2_2.configure(anchor='w')
    Label2_2.configure(background="#e6fdff")
    Label2_2.configure(compound='left')
    Label2_2.configure(disabledforeground="#a3a3a3")
    Label2_2.configure(font="-family {Courier New} -size 12")
    Label2_2.configure(foreground="#000000")
    Label2_2.configure(highlightbackground="#d9d9d9")
    Label2_2.configure(highlightcolor="black")
    Label2_2.configure(text='''Режим''')

    fileOUTE = Entry(desfW)
    fileOUTE.place(relx=0.017, rely=0.847, height=30, relwidth=0.957)
    fileOUTE.configure(background="white")
    fileOUTE.configure(disabledforeground="#a3a3a3")
    fileOUTE.configure(font="TkFixedFont")
    fileOUTE.configure(foreground="#000000")
    fileOUTE.configure(insertbackground="black")

    Label2_3 = Label(desfW)
    Label2_3.place(relx=0.017, rely=0.78, height=17, width=144)
    Label2_3.configure(activebackground="#f9f9f9")
    Label2_3.configure(anchor='w')
    Label2_3.configure(background="#e6fdff")
    Label2_3.configure(compound='left')
    Label2_3.configure(disabledforeground="#a3a3a3")
    Label2_3.configure(font="-family {Courier New} -size 12")
    Label2_3.configure(foreground="#000000")
    Label2_3.configure(highlightbackground="#d9d9d9")
    Label2_3.configure(highlightcolor="black")
    Label2_3.configure(text='''Сохранено в''')

    keyFile_in = Button(desfW, command=openKey)
    keyFile_in.place(relx=0.283, rely=0.441, height=24, width=47)
    keyFile_in.configure(activebackground="beige")
    keyFile_in.configure(activeforeground="#000000")
    keyFile_in.configure(background="#d9d9d9")
    keyFile_in.configure(compound='left')
    keyFile_in.configure(disabledforeground="#a3a3a3")
    keyFile_in.configure(font="-family {Segoe UI} -size 7")
    keyFile_in.configure(foreground="#000000")
    keyFile_in.configure(highlightbackground="#d9d9d9")
    keyFile_in.configure(highlightcolor="black")
    keyFile_in.configure(pady="0")
    keyFile_in.configure(text='''Открыть''')

    keyFile_out = Button(desfW, command=saveKey)
    keyFile_out.place(relx=0.383, rely=0.441, height=24, width=47)
    keyFile_out.configure(activebackground="beige")
    keyFile_out.configure(activeforeground="#000000")
    keyFile_out.configure(background="#d9d9d9")
    keyFile_out.configure(compound='left')
    keyFile_out.configure(disabledforeground="#a3a3a3")
    keyFile_out.configure(font="-family {Segoe UI} -size 7")
    keyFile_out.configure(foreground="#000000")
    keyFile_out.configure(highlightbackground="#d9d9d9")
    keyFile_out.configure(highlightcolor="black")
    keyFile_out.configure(pady="0")
    keyFile_out.configure(text='''Сохранить''')

    ivFile_in = Button(desfW, command=openIV)
    ivFile_in.place(relx=0.8, rely=0.441, height=24, width=47)
    ivFile_in.configure(activebackground="beige")
    ivFile_in.configure(activeforeground="#000000")
    ivFile_in.configure(background="#d9d9d9")
    ivFile_in.configure(compound='left')
    ivFile_in.configure(disabledforeground="#a3a3a3")
    ivFile_in.configure(font="-family {Segoe UI} -size 7")
    ivFile_in.configure(foreground="#000000")
    ivFile_in.configure(highlightbackground="#d9d9d9")
    ivFile_in.configure(highlightcolor="black")
    ivFile_in.configure(pady="0")
    ivFile_in.configure(text='''Открыть''')

    ivFile_out = Button(desfW, command=saveIV)
    ivFile_out.place(relx=0.9, rely=0.441, height=24, width=47)
    ivFile_out.configure(activebackground="beige")
    ivFile_out.configure(activeforeground="#000000")
    ivFile_out.configure(background="#d9d9d9")
    ivFile_out.configure(compound='left')
    ivFile_out.configure(disabledforeground="#a3a3a3")
    ivFile_out.configure(font="-family {Segoe UI} -size 7")
    ivFile_out.configure(foreground="#000000")
    ivFile_out.configure(highlightbackground="#d9d9d9")
    ivFile_out.configure(highlightcolor="black")
    ivFile_out.configure(pady="0")
    ivFile_out.configure(text='''Сохранить''')
