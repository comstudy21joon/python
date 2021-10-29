from tkinter import Tk
from tkinter.ttk import Label, Button

win = Tk();

lbl = Label(win, text="결과: 아래 버튼을 누르세요");
btn1 = Button(win, text="확인")
btn2 = Button(win, text="취소")

lbl.pack()
btn1.pack()
btn2.pack()

if __name__ == '__main__':
    win.mainloop();
