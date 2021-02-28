from tkinter import Button, END, Text, Tk
import re
from math import sqrt

root = Tk()
root.title("calculator")
root.geometry("380x380+450+50")
root.configure(bg="#36454f")
root.resizable(width=0, height=0)


def calculate():
    get_all = entry.get(1.0, END)
    value = get_all
    value = re.sub(u"\u00F7", "/", value)
    value = re.sub("X", "*", value)
    value = re.sub("%", "/100", value)
    answer = eval(value)
    entry.delete(1.0, END)
    entry.insert(1.0, answer)


def clear():
    entry.delete(1.0, END)


def buttons(text):
    entry.insert(END, text)


def squareroot():
    get_all = entry.get(1.0, END)
    value = get_all
    answer = sqrt(int(value))
    entry.delete(1.0, END)
    entry.insert(1.0, answer)


entry = Text(root, width=30, height=2, bg="white", bd=10, font="5")
entry.place(x=43, y=10)


def all_buttons():
    button_nine = Button(root, text="9", width=8, bd=5,
                         font="1", bg="#737373", command=lambda: buttons("9"))
    button_nine.place(x=10, y=100)
    button_eight = Button(root, text="8", width=8, bd=5,
                          font="1", bg="#737373", command=lambda: buttons("8"))
    button_eight.place(x=100, y=100)
    button_seven = Button(root, text="7", width=8, bd=5,
                          font="1", bg="#737373", command=lambda: buttons("7"))
    button_seven.place(x=190, y=100)
    button_six = Button(root, text="6", width=8, bd=5,
                        font="1", bg="#737373", command=lambda: buttons("6"))
    button_six.place(x=10, y=150)
    button_five = Button(root, text="5", width=8, bd=5,
                         font="1", bg="#737373", command=lambda: buttons("5"))
    button_five.place(x=100, y=150)
    button_four = Button(root, text="4", width=8, bd=5,
                         font="1", bg="#737373", command=lambda: buttons("4"))
    button_four.place(x=190, y=150)
    button_three = Button(root, text="3", width=8, bd=5,
                          font="1", bg="#737373", command=lambda: buttons("3"))
    button_three.place(x=10, y=200)
    button_two = Button(root, text="2", width=8, bd=5,
                        font="1", bg="#737373", command=lambda: buttons("2"))
    button_two.place(x=100, y=200)
    button_one = Button(root, text="1", width=8, bd=5,
                        font="1", bg="#737373", command=lambda: buttons("1"))
    button_one.place(x=190, y=200)
    button_zero = Button(root, bg="#737373", text="0", width=8, bd=5,
                         font="1", command=lambda: buttons("0"))
    button_zero.place(x=10, y=250)
    button_dot = Button(root, text=u"\u2022", width=8, bd=5,
                        font="1", bg="#ff6500", command=lambda: buttons("."))
    button_dot.place(x=100, y=250)
    button_plus = Button(root, text="+", width=8, bd=5,
                         font="1", bg="#ff6500", command=lambda: buttons("+"))
    button_plus.place(x=280, y=250)
    button_minus = Button(root, text="-", width=8, bd=5,
                          font="1", bg="#ff6500", command=lambda: buttons("-"))
    button_minus.place(x=280, y=200)
    button_div = Button(root, text=u"\u00F7", width=8, bd=5,
                        font="1", bg="#ff6500", command=lambda: buttons(u"\u00F7"))
    button_div.place(x=280, y=100)
    button_multi = Button(root, text="x", width=8, bd=5,
                          font="1", bg="#ff6500", command=lambda: buttons("X"))
    button_multi.place(x=280, y=150)
    button_squareroot = Button(root, text=u'\u221a', width=8, bd=5,
                               font="1", height=2, bg="#ff6500", command=lambda: squareroot())
    button_squareroot.place(x=10, y=300)
    button_percent = Button(root, text="%", width=8, bd=5,
                            font="1", bg="#ff6500", command=lambda: buttons("%"))
    button_percent.place(x=190, y=250)
    button_clear = Button(root, text=u"\u232B", width=13, bd=5,
                          font="1", height=2, bg="#ff6500", command=lambda: clear())
    button_clear.place(x=100, y=300)
    button_calc = Button(root, text="=", width=13, height=2,
                         bd=5, font="1", bg="#ff6500", command=calculate)
    button_calc.place(x=236, y=300)


all_buttons()

root.mainloop()
