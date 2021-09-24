"""
from tkinter import Tk, PanedWindow, Menu, LabelFrame
from tkinter.ttk import Label, Entry, Button

win = Tk()

menu_area = Menu(win)
win.configure(menu=menu_area)

menu1 = Menu(menu_area)
menu1.add_command(label="New...")
menu_area.add_cascade(label="File", menu=menu1)

label_frame = LabelFrame(win, text='label frame')
label_frame.grid(row=0, column=0, padx=5, pady=5)

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

panedwindow=PanedWindow(relief="raised", bd=0)
panedwindow.grid(row=3,column=0, columnspan=2, padx=5, pady=5)

btn_ok = Button(panedwindow, text="확인")
btn_cancel = Button(panedwindow, text="취소")

panedwindow.add(btn_ok)
panedwindow.add(btn_cancel)

if __name__ == '__main__':
    win.mainloop()
"""


"""
win = Tk()
win.geometry('%dx%d+%d+%d' %(800, 600, 5, 5))


topFrame = Frame(win)
topFrame.pack(side='top')
topFrame.config(width=800, height=100, background="orange")


panedwindow=PanedWindow(relief="raised", bd=0)
panedwindow.pack(expand=True)

leftFrame = Frame(win)
leftFrame.pack(side='left')
leftFrame.config(width=200, height=400, background="red")

rightFrame = Frame(win)
rightFrame.pack(side='right')
rightFrame.config(width=600, height=400, background="green")

panedwindow.add(leftFrame)
panedwindow.add(rightFrame)

bottomFrame = Frame(win)
bottomFrame.pack(side='bottom')
bottomFrame.config(width=800, height=100, background="blue")

win.mainloop()
"""



"""
win = Tk()
win.geometry('%dx%d+%d+%d' %(800, 600, 5, 5))


topFrame = Frame(win)
topFrame.pack(side='top')
topFrame.config(width=800, height=100, background="orange")


panedwindow=PanedWindow(relief="raised", bd=0)
panedwindow.pack(expand=True)

leftFrame = Frame(win)
leftFrame.pack(side='left')
leftFrame.config(width=200, height=400, background="")

rightFrame = Frame(win)
rightFrame.pack(side='right')
rightFrame.config(width=600, height=400, background="green")

panedwindow.add(leftFrame)
panedwindow.add(rightFrame)

bottomFrame = Frame(win)
bottomFrame.pack(side='bottom')
bottomFrame.config(width=800, height=100, background="blue")

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

win.mainloop()
"""



"""
win = Tk()
win.geometry('%dx%d+%d+%d' %(800, 600, 5, 5))


topFrame = Frame(win)
topFrame.pack(side='top')
topFrame.config(width=800, height=100, background="orange")


panedwindow=PanedWindow(relief="raised", bd=0)
panedwindow.pack(expand=True)

leftFrame = Frame(win)
leftFrame.pack(side='left')
leftFrame.config(width=200, height=400, background="")

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
btn_cancel = Button(panedwindow, text="취소")

panedwindow.add(btn_output)
panedwindow.add(btn_input)
panedwindow.add(btn_search)
panedwindow.add(btn_modify)
panedwindow.add(btn_delete)
panedwindow.add(btn_cancel)

win.mainloop()
"""



from tkinter import Tk, Frame, PanedWindow, ttk
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
btn_cancel = Button(panedwindow, text="취소")

panedwindow.add(btn_output)
panedwindow.add(btn_input)
panedwindow.add(btn_search)
panedwindow.add(btn_modify)
panedwindow.add(btn_delete)
panedwindow.add(btn_cancel)


# rightFrame에 목록 추가하기
header_list = ['no', 'name', 'phone number', 'e-mail']
data_list = [
(1,'kim', '010-1111-1111', 'kim@comstudy21.or.kr'),
(2,'lee', '010-1111-1111', 'lee@comstudy21.or.kr'),
(3,'park', '010-1111-1111', 'park@comstudy21.or.kr'),
(4,'kang', '010-1111-1111', 'kang@comstudy21.or.kr')
]

tree = ttk.Treeview(rightFrame, columns=header_list, show="headings")
tree.pack()

for i, col in enumerate(header_list):
    tree.heading(col, text=col.title())
for item in data_list:
    tree.insert('', 'end', values=item)

# TreeView의 각 필드 너비 설정
tree.column(0, width=50)
tree.column(1, width=80)
tree.column(2, width=150)
tree.column(3, width=250)

# TreeView의 높이 설정
tree.config(height=22)

# 앱 타이틀 라벨 추가
fontStyle = tkFont.Font(family="궁서체", size=28)
lbl_title = Label(topFrame, text="고객 관리 시스템", font=fontStyle)
#lbl_title.pack(side="bottom", anchor="center")
lbl_title.place(relx=0.5, rely=0.5, anchor='center')
#lbl_title.config(background="red")

win.mainloop()




"""
from tkinter import Tk, PanedWindow, Menu, LabelFrame
from tkinter.ttk import Label, Entry, Button

def btnEvtHandler() :
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    lbl_ressult.config(text="%s, %s, %s" %(name, phone, email))

win = Tk()

label_frame = LabelFrame(win, text='label frame')
label_frame.grid(row=0, column=0, padx=5, pady=5)

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

panedwindow=PanedWindow(relief="raised", bd=0)
panedwindow.grid(row=3,column=0, columnspan=2, padx=5, pady=5)

btn_ok = Button(panedwindow, text="확인", command=btnEvtHandler)
btn_cancel = Button(panedwindow, text="취소")

panedwindow.add(btn_ok)
panedwindow.add(btn_cancel)

lbl_ressult = Label(win, text="결과:")
lbl_ressult.grid(row=1, column=0)

if __name__ == '__main__':
    win.mainloop()
"""



