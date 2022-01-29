from tkinter import Tk, Frame, PanedWindow, ttk, messagebox
from tkinter.ttk import Labelframe, Label, Entry, Button
import tkinter.font as tkFont

def deleteTreeData() :
    children = tree.get_children()
    if children != '()':
        for item in children:
            tree.delete(item)

def refreshTreeData(data_list) :
    for i, item in enumerate(data_list):
        tree.insert('', 'end', iid='IID%d' % (i), values=item)

def refreshTreeview(data_list) :
    deleteTreeData()
    refreshTreeData(data_list)

# 이벤트 핸들러
def outputEvtHandler():
    #print("전체 보기 ...")
    refreshTreeview(data_list)

seq = 5
def inputEvtHandler():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    if name=="" or phone=="" or email=="" :
        messagebox.showinfo('알림', '이름, 전화번호, 이메일을 모두 입력 하세요!')
        return

    global seq
    data_list.append((seq, name, phone, email))
    #tree.insert('', 'end', values=(seq, name, phone, email))
    seq += 1

    refreshTreeview(data_list)


def searchEvtHandler():
    #print("검색 ...")
    sname = entry_name.get()
    if sname == "" :
        messagebox.showinfo('경고','이름을 입력 하고 검색 하세요!')
        return

    #search_data_list = [(2,'lee', '010-1111-1111', 'lee@comstudy21.or.kr')]
    search_data_list = []
    for data in data_list :
        try :
            idx = data.index(sname)
            search_data_list.append(data)
        except :
            pass
    if search_data_list == [] :
        messagebox.showinfo('경고', '찾는 정보가 없습니다!')
        return

    #print(search_data_list)
    refreshTreeview(search_data_list)

def modifyEvtHandler():
    print("수정 ...")
    sname = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    if sname == "" or phone == "" or email == "":
        messagebox.showinfo('알림', '이름, 전화번호, 이메일을 모두 입력 하세요!')
        return

    idx = -1
    for i, data in enumerate(data_list) :
        try :
            idx = data.index(sname)
            data_list[i] = (data[0], sname, phone, email)
            refreshTreeview(data_list)
            return
        except :
            pass

    print(idx)
    if idx == -1 :
        messagebox.showinfo('경고', '찾는 정보가 없습니다!')




def deleteEvtHandler():
    print("삭제 ...")
    sname = entry_name.get()
    if sname == "":
        messagebox.showinfo('경고', '이름을 입력 하고 검색 하세요!')
        return

    idx = -1
    for data in data_list:
        try:
            idx = data.index(sname)
            del data_list[data_list.index(data)]
            refreshTreeview(data_list)
        except:
            pass

    if idx == -1 :
        messagebox.showinfo('경고', '찾는 정보가 없습니다!')


def backupEvtHandler():
    print("파일로 백업 ...")


def loadEvtHandler():
    print("파일로 로드 ...")



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

btn_output = Button(panedwindow, text="전체보기", command=outputEvtHandler)
btn_input = Button(panedwindow, text="입력", command=inputEvtHandler)
btn_search = Button(panedwindow, text="검색", command=searchEvtHandler)
btn_modify = Button(panedwindow, text="수정", command=modifyEvtHandler)
btn_delete = Button(panedwindow, text="삭제", command=deleteEvtHandler)
btn_backup = Button(panedwindow, text="파일백업", command=backupEvtHandler)
btn_load = Button(panedwindow, text="파일로드", command=loadEvtHandler)

panedwindow.add(btn_output)
panedwindow.add(btn_input)
panedwindow.add(btn_search)
panedwindow.add(btn_modify)
panedwindow.add(btn_delete)
panedwindow.add(btn_backup)
panedwindow.add(btn_load)


# rightFrame에 목록 추가하기
header_list = ['no', 'name', 'phone number', 'e-mail']
data_list = [
(1,'kim', '010-2222-1111', 'kim@comstudy21.or.kr'),
(2,'lee', '010-2222-2222', 'lee@comstudy21.or.kr'),
(3,'park', '010-2222-3333', 'park@comstudy21.or.kr'),
(4,'kang', '010-2222-4444', 'kang@comstudy21.or.kr')
]


tree = ttk.Treeview(rightFrame, columns=header_list, show="headings")
tree.pack()

for i, col in enumerate(header_list):
    tree.heading(col, text=col.title())
for i, item in enumerate(data_list):
    tree.insert('', 'end', iid='IID%d' %(i), values=item)

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


# tree의 행을 클릭하면 정보가 입력 된다.
def click_item(event) :
    treeFous = tree.focus()
    treeItemValue = tree.item(treeFous).get('values')
    #print(treeItemValue)
    if len(entry_name.get()) != 0 : entry_name.delete(0,'end')
    if len(entry_phone.get()) != 0: entry_phone.delete(0, 'end')
    if len(entry_email.get()) != 0: entry_email.delete(0, 'end')
    entry_name.insert(0, treeItemValue[1])
    entry_phone.insert(0, treeItemValue[2])
    entry_email.insert(0, treeItemValue[3])

tree.bind('<ButtonRelease-1>', click_item)


if __name__ == '__main__':
    win.mainloop()


####################### Step04. 목록 만들기 ############################