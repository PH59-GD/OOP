import tkinter as tk
from tkinter import *

top = Tk()

top.geometry("500x500")


answer = Text(width=35, height=2)
answer.place(x=100, y=100)

def show(x):
    try:
        if x == "=":
            final_answer = eval(answer.get(1.0, "end-1c"))
            answer.insert(tk.INSERT, x)
            answer.insert(tk.INSERT, final_answer)
        elif x == "Clear":
            answer.delete(1.0, END)
        else:
            answer.insert(tk.INSERT, x)

    except:
        answer.delete(1.0,END)

B1 = Button(top, text="1", width=10, height=3, command=lambda: show("1"))
B1.place(x=100, y=220)
B2 = Button(top, text="2", width=10, height=3, command=lambda: show("2"))
B2.place(x=200, y=220)
B3 = Button(top, text="3", width=10, height=3, command=lambda: show("3"))
B3.place(x=300, y=220)
B4 = Button(top, text="4", width=10, height=3, command=lambda: show("4"))
B4.place(x=100, y=300)
B5 = Button(top, text="5", width=10, height=3, command=lambda: show("5"))
B5.place(x=200, y=300)
B6 = Button(top, text="6", width=10, height=3, command=lambda: show("6"))
B6.place(x=300, y=300)
B7 = Button(top, text="7", width=10, height=3, command=lambda: show("7"))
B7.place(x=100, y=380)
B8 = Button(top, text="8", width=10, height=3, command=lambda: show("8"))
B8.place(x=200, y=380)
B9 = Button(top, text="9", width=10, height=3, command=lambda: show("9"))
B9.place(x=300, y=380)
B0 = Button(top, text="0", width=10, height=2, command=lambda: show("0"))
B0.place(x=200, y=450)
BE = Button(top, text="=", width=10, height=2, command=lambda: show("="))
BE.place(x=300, y=450)
BP = Button(top, text="+", width=10, height=2, command=lambda: show("+"))
BP.place(x=100, y=450)
BM = Button(top, text="-", width=10, height=3, command=lambda: show("-"))
BM.place(x=0, y=380)
BD = Button(top, text="/", width=10, height=3, command=lambda: show("/"))
BD.place(x=0, y=300)
BML = Button(top, text="*", width=10, height=3, command=lambda: show("*"))
BML.place(x=0, y=220)
BC = Button(top, text="Clear", width=10, height=2, command=lambda: show("Clear"))
BC.place(x=0, y=450)



top.mainloop()
