#MIT License

#Copyright (c) 2022 Fazz

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

from tkinter import *

#Pencere Ayarları
root = Tk()
root.geometry("500x500+550+150")
bg = PhotoImage(file = "background.png")
label1 = Label( root, image = bg, bg="#4B524E")
label1.place(x = 0, y = 0)
root.title("Tic Tac Toe | FazzTech")
root.resizable(width=False, height=False)
root.iconbitmap(default='logo.ico')

#Değişkenler
xbas = "X"
obas = "O"
bosluk = " "


#Fonksiyonlar

def buton1bas():
    if label2["text"] == "Sıra : X" and buton1["text"]==bosluk:
        buton1["text"] = "X"
        label2["text"] = "Sıra : O"
    elif label2["text"] == "Sıra : O" and buton1["text"]==bosluk:
        buton1["text"] = "O"
        label2["text"] = "Sıra : X"

def buton2bas():
    if label2["text"] == "Sıra : X" and buton2["text"]==bosluk:
        buton2["text"] = "X"
        label2["text"] = "Sıra : O"
    elif label2["text"] == "Sıra : O" and buton2["text"]==bosluk:
        buton2["text"] = "O"
        label2["text"] = "Sıra : X"


def buton3bas():
    if label2["text"] == "Sıra : X" and buton3["text"]==bosluk:
        buton3["text"] = "X"
        label2["text"] = "Sıra : O"
    elif label2["text"] == "Sıra : O" and buton3["text"]==bosluk:
        buton3["text"] = "O"
        label2["text"] = "Sıra : X"

def buton4bas():
    if label2["text"] == "Sıra : X" and buton4["text"]==bosluk:
        buton4["text"] = "X"
        label2["text"] = "Sıra : O"
    elif label2["text"] == "Sıra : O" and buton4["text"]==bosluk:
        buton4["text"] = "O"
        label2["text"] = "Sıra : X"

def buton5bas():
    if label2["text"] == "Sıra : X" and buton5["text"]==bosluk:
        buton5["text"] = "X"
        label2["text"] = "Sıra : O"
    elif label2["text"] == "Sıra : O" and buton5["text"]==bosluk:
        buton5["text"] = "O"
        label2["text"] = "Sıra : X"

def buton6bas():
    if label2["text"] == "Sıra : X" and buton6["text"]==bosluk:
        buton6["text"] = "X"
        label2["text"] = "Sıra : O"
    elif label2["text"] == "Sıra : O" and buton6["text"]==bosluk:
        buton6["text"] = "O"
        label2["text"] = "Sıra : X"

def buton7bas():
    if label2["text"] == "Sıra : X" and buton7["text"]==bosluk:
        buton7["text"] = "X"
        label2["text"] = "Sıra : O"
    elif label2["text"] == "Sıra : O" and buton7["text"]==bosluk:
        buton7["text"] = "O"
        label2["text"] = "Sıra : X"

def buton8bas():
    if label2["text"] == "Sıra : X" and buton8["text"]==bosluk:
        buton8["text"] = "X"
        label2["text"] = "Sıra : O"
    elif label2["text"] == "Sıra : O" and buton8["text"]==bosluk:
        buton8["text"] = "O"
        label2["text"] = "Sıra : X"

def buton9bas():
    if label2["text"] == "Sıra : X" and buton9["text"]==bosluk:
        buton9["text"] = "X"
        label2["text"] = "Sıra : O"
    elif label2["text"] == "Sıra : O" and buton9["text"]==bosluk:
        buton9["text"] = "O"
        label2["text"] = "Sıra : X"

def xkazan():
    if buton1["text"]=="X" and buton2["text"]=="X" and buton3["text"]=="X":
        label3["text"]="Kazanan : X"
    elif buton1["text"]=="O" and buton2["text"]=="O" and buton3["text"]=="O":
        label3["text"]="Kazanan : O"
    elif buton4["text"]=="X" and buton5["text"]=="X" and buton6["text"]=="X":
        label3["text"]="Kazanan : X"
    elif buton4["text"]=="O" and buton5["text"]=="O" and buton6["text"]=="O":
        label3["text"]="Kazanan : O"
    elif buton7["text"]=="X" and buton8["text"]=="X" and buton9["text"]=="X":
        label3["text"]="Kazanan : X"
    elif buton7["text"]=="O" and buton8["text"]=="O" and buton9["text"]=="O":
        label3["text"]="Kazanan : O"
    elif buton1["text"]=="X" and buton5["text"]=="X" and buton9["text"]=="X":
        label3["text"]="Kazanan : X"
    elif buton1["text"]=="O" and buton5["text"]=="O" and buton9["text"]=="O":
        label3["text"]="Kazanan : O"
    elif buton3["text"]=="X" and buton5["text"]=="X" and buton7["text"]=="X":
        label3["text"]="Kazanan : X"
    elif buton3["text"]=="O" and buton5["text"]=="O" and buton7["text"]=="O":
        label3["text"]="Kazanan : O"
    elif buton1["text"]=="X" and buton4["text"]=="X" and buton7["text"]=="X":
        label3["text"]="Kazanan : X"
    elif buton2["text"]=="O" and buton5["text"]=="O" and buton8["text"]=="O":
        label3["text"]="Kazanan : O"
    elif buton3["text"]=="X" and buton6["text"]=="X" and buton9["text"]=="X":
        label3["text"]="Kazanan : X"
    elif buton3["text"]=="O" and buton6["text"]=="O" and buton9["text"]=="O":
        label3["text"]="Kazanan : O"
    elif buton2["text"]=="X" and buton5["text"]=="X" and buton8["text"]=="X":
        label3["text"]="Kazanan : X"
    elif buton2["text"]=="O" and buton5["text"]=="O" and buton8["text"]=="O":
        label3["text"]="Kazanan : O"

def yeniden():
    buton1["text"]=bosluk
    buton2["text"]=bosluk
    buton3["text"]=bosluk
    buton4["text"]=bosluk
    buton5["text"]=bosluk
    buton6["text"]=bosluk
    buton7["text"]=bosluk
    buton8["text"]=bosluk
    buton9["text"]=bosluk
    label3["text"]="Kazanan : 0"

#Buton ve Label

buton1 = Button(bg="#4B524E", text=bosluk, fg="black", command=lambda:[buton1bas(), xkazan()])
buton1.place(x=150, y=140, width=65, height=65)

buton2 = Button(bg="#4B524E", text=bosluk, fg="black",command=lambda:[buton2bas(), xkazan()])
buton2.place(x=220, y=140, width=65, height=65)

buton3 = Button(bg="#4B524E", text=bosluk, fg="black", command=lambda:[buton3bas(), xkazan()])
buton3.place(x=290, y=140, width=65, height=65,)

buton4 = Button(bg="#4B524E", text=bosluk, fg="black", command=lambda:[buton4bas(), xkazan()])
buton4.place(x=150, y=220, width=65, height=65)

buton5 = Button(bg="#4B524E", text=bosluk, fg="black", command=lambda:[buton5bas(), xkazan()])
buton5.place(x=220, y=220, width=65, height=65)

buton6 = Button(bg="#4B524E", text=bosluk, fg="black", command=lambda:[buton6bas(), xkazan()])
buton6.place(x=290, y=220, width=65, height=65)

buton7 = Button(bg="#4B524E", text=bosluk, fg="black", command=lambda:[buton7bas(), xkazan()])
buton7.place(x=150, y=300, width=65, height=65)

buton8 = Button(bg="#4B524E", text=bosluk, fg="black", command=lambda:[buton8bas(), xkazan()])
buton8.place(x=220, y=300, width=65, height=65)

buton9 = Button(bg="#4B524E", text=bosluk, fg="black", command=lambda:[buton9bas(), xkazan()])
buton9.place(x=290, y=300, width=65, height=65)

buton10 = Button(text="Yeniden Başlat", fg="Red", font="Ariel 18", command=yeniden)
buton10.place(x=160, y=400)


label2 = Label(text="Sıra : X", bg="#4B524E", fg="white", font="Courier")
label2.place(x=10, y=160)

label3 = Label(text="Kazanan : 0", bg="#4B524E", fg="white", font="Courier")
label3.place(x=10, y=190)

label5 = Label(text="Tic Tac Toe Game", bg="#4B524E", fg="Green", font="Arial 20")
label5.place(x=135, y=70)

root.mainloop()