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
leftFrame.config(width=200, height=400, background="#eee")

rightFrame = Frame(win)
rightFrame.pack(side='right')
rightFrame.config(width=600, height=470, background="green")

panedwindow.add(leftFrame)
panedwindow.add(rightFrame)

bottomFrame = Frame(win)
bottomFrame.pack(side='bottom')
bottomFrame.config(width=800, height=30, background="blue")


# leftFrame에 Entry 위젯 추가
label_frame = Labelframe(leftFrame, text='기본 정보 입력')
label_frame.pack()

lbl_name = Label(label_frame, text="성명:")
lbl_phone = Label(label_frame, text="전화번호:")
lbl_email = Label(label_frame, text="이메일:")

entry_name = Entry(label_frame)
entry_phone = Entry(label_frame)
entry_email = Entry(label_frame)

lbl_name.grid(row=0, column=0)
entry_name.grid(row=0, column=1, padx=5, pady=5)
lbl_phone.grid(row=1, column=0)
entry_phone.grid(row=1, column=1, padx=5, pady=5)
lbl_email.grid(row=2, column=0)
entry_email.grid(row=2, column=1, padx=5, pady=5)


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


####################### Step02. 입력 Entry 창 만들기 ############################