from tkinter import Tk
from tkinter.ttk import Label, Entry, Button

win = Tk()

lbl_name = Label(win, text="성명:")
lbl_phone = Label(win, text="전화번호:")
lbl_email = Label(win, text="이메일:")

entry_name = Entry(win)
entry_phone = Entry(win)
entry_email = Entry(win)

btn_ok = Button(win, text="확인")
btn_cancel = Button(win, text="취소")

lbl_name.pack()
entry_name.pack()
lbl_phone.pack()
entry_phone.pack()
lbl_email.pack()
entry_email.pack()

btn_ok.pack()
btn_cancel.pack()

if __name__ == '__main__':
    win.mainloop()