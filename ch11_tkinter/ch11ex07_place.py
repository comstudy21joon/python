from tkinter import Tk, PanedWindow
from tkinter.ttk import Label, Entry, Button

win = Tk()
win.geometry("210x130+100+100")

lbl_name = Label(win, text="성명:")
lbl_phone = Label(win, text="전화번호:")
lbl_email = Label(win, text="이메일:")

entry_name = Entry(win)
entry_phone = Entry(win)
entry_email = Entry(win)

lbl_name.place(x=0, y=10)
entry_name.place(x=60, y=10)
lbl_phone.place(x=0, y=40)
entry_phone.place(x=60, y=40)
lbl_email.place(x=0, y=70)
entry_email.place(x=60, y=70)

panedwindow=PanedWindow(relief="raised", bd=0)
panedwindow.place(x=20, y=100)

btn_ok = Button(panedwindow, text="확인")
btn_cancel = Button(panedwindow, text="취소")

panedwindow.add(btn_ok)
panedwindow.add(btn_cancel)

if __name__ == '__main__':
    win.mainloop()