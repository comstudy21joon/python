from tkinter import Tk, PanedWindow
from tkinter.ttk import Label, Button, Entry

win = Tk()

lbl = Label(win, text="성명 : ")
entry = Entry(win)

lbl.pack()
entry.pack()

panedwindow=PanedWindow(relief="raised", bd=0)
panedwindow.pack(expand=True)

btn_ok = Button(panedwindow, text="확인")
btn_cancel = Button(panedwindow, text="취소")

panedwindow.add(btn_ok)
panedwindow.add(btn_cancel)

if __name__ == '__main__':
    win.mainloop()