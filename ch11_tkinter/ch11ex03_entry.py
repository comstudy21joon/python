from tkinter import Tk
from tkinter.ttk import Label, Button, Entry

win = Tk();

lbl = Label(win, text="성명 : ")
entry = Entry(win)
btn = Button(win, text="확인")

lbl.pack()
entry.pack()
btn.pack()

if __name__ == '__main__':
    win.mainloop();
