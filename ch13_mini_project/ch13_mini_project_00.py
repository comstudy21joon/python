from tkinter import Tk, Frame, PanedWindow, ttk, messagebox
from tkinter.ttk import Labelframe, Label, Entry, Button
import tkinter.font as tkFont


win = Tk()
win.geometry('%dx%d+%d+%d' %(800, 600, 5, 5))

topFrame = Frame(win)
topFrame.pack(side='top')
topFrame.config(width=800, height=100, background="#eee")

panedwindow=PanedWindow(relief="raised", bd=0)
panedwindow.pack(expand=True)

leftFrame = Frame(win)
leftFrame.pack(side='left')
leftFrame.config(width=200, height=400, background="orange")

rightFrame = Frame(win)
rightFrame.pack(side='right')
rightFrame.config(width=600, height=470, background="green")

panedwindow.add(leftFrame)
panedwindow.add(rightFrame)

bottomFrame = Frame(win)
bottomFrame.pack(side='bottom')
bottomFrame.config(width=800, height=30, background="blue")

# bottomFrame에 Button 위젯 추가하기
panedwindow=PanedWindow(bottomFrame, relief="raised", bd=0)
panedwindow.pack()

btn_output = Button(panedwindow, text="전체보기")
btn_input = Button(panedwindow, text="입력")
btn_search = Button(panedwindow, text="검색")
btn_modify = Button(panedwindow, text="수정")
btn_delete = Button(panedwindow, text="삭제")
btn_backup = Button(panedwindow, text="파일백업")
btn_load = Button(panedwindow, text="파일로드")

panedwindow.add(btn_output)
panedwindow.add(btn_input)
panedwindow.add(btn_search)
panedwindow.add(btn_modify)
panedwindow.add(btn_delete)
panedwindow.add(btn_backup)
panedwindow.add(btn_load)

# 앱 타이틀 라벨 추가
fontStyle = tkFont.Font(family="궁서체", size=28)
lbl_title = Label(topFrame, text="고객 관리 시스템", font=fontStyle)
lbl_title.place(relx=0.5, rely=0.5, anchor='center')


if __name__ == '__main__':
    win.mainloop()


####################### Step01. 레이아웃 만들기 ############################