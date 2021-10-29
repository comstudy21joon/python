from tkinter import Tk, PanedWindow
from tkinter.ttk import Label, Entry, Button

win = Tk()

lbl_name = Label(win, text="성명:")
lbl_phone = Label(win, text="전화번호:")
lbl_email = Label(win, text="이메일:")

entry_name = Entry(win)
entry_phone = Entry(win)
entry_email = Entry(win)

lbl_name.grid(row=0, column=0)
entry_name.grid(row=0, column=1)
lbl_phone.grid(row=1, column=0)
entry_phone.grid(row=1, column=1)
lbl_email.grid(row=2, column=0)
entry_email.grid(row=2, column=1)

panedwindow=PanedWindow(relief="raised", bd=0)
panedwindow.grid(row=3,column=0, columnspan=2)

btn_ok = Button(panedwindow, text="확인")
btn_cancel = Button(panedwindow, text="취소")

panedwindow.add(btn_ok)
panedwindow.add(btn_cancel)

if __name__ == '__main__':
    win.mainloop()