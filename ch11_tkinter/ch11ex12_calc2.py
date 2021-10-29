from tkinter import Tk, Button, Entry, END

opers = []
nums = []
numStr = '';

def calc(target) :
    ch = target['text']
    global opers, nums, numStr
    if len(ch) == 1 :
        if ch != 'C' and ch != '%' and ch != 'v': txt_result.insert(END, ch)
        if ord(ch) >= 48 and ord(ch) <= 57 :
            numStr += ch;
        if ch=='+' or ch=='-' or ch=='*' or ch=='/' :
            nums.append(numStr)
            opers.append(ch)
            numStr = '';
        if ch == '=' :
            nums.append(numStr)
            # print(nums)
            # print(opers)
            result = int(nums[0]);
            for i, oper in enumerate(opers) :
                if oper == '+' :
                    result += int(nums[i+1])
                elif oper == '-' :
                    result -= int(nums[i + 1])
                elif oper == '*' :
                    result *= int(nums[i + 1])
                elif oper == '/' :
                    result //= int(nums[i + 1])

            txt_result.insert(END, str(result))


win = Tk()

# 첫번째 줄에는 텍스트가 표시 되도록 Entry 위젯
txt_result = Entry(win, width=26, justify="right")
txt_result.grid(row=0, column=0, columnspan=5, pady=2)


# 두번째 줄 부터는 계산기 버튼 위젯
btns = [
    [Button(win, text="MC"),Button(win, text="MR"),Button(win, text="MS"),Button(win, text="M+"),Button(win, text="M-")],
    [Button(win, text="<-"),Button(win, text="CE"),Button(win, text="C"),Button(win, text="+-"),Button(win, text="v")],
    [Button(win, text="7"),Button(win, text="8"),Button(win, text="9"),Button(win, text="/"),Button(win, text="%")],
    [Button(win, text="4"),Button(win, text="5"),Button(win, text="6"),Button(win, text="*"),Button(win, text="1/x")],
    [Button(win, text="1"),Button(win, text="2"),Button(win, text="3"),Button(win, text="-"),Button(win, text="=")],
    [Button(win, text="0"),Button(win, text="."),Button(win, text="+")]
]

# 버튼에 이벤트 핸들러를 등록 할때 개별 버튼을 인수로 전달
for btnArr in btns :
    for btn in btnArr :
        def clickEvent(target = btn):
            calc(target)
        btn.config(command=clickEvent)

for i in range(1,6) :
    for j in range(5) :
        if i == 6 and j == 3:
            break
        if i == 5 and j == 4 :
            btns[i - 1][j].grid(row=i, column=j, rowspan=2, sticky='wens', padx=2, pady=2)
        else :
            btns[i - 1][j].grid(row=i, column=j, padx=2, pady=2, sticky='wens')

btns[5][0].grid(row=6, column=0, columnspan=2, sticky='wens', padx=2, pady=2)
btns[5][1].grid(row=6, column=2, padx=2, pady=2, sticky='wens')
btns[5][2].grid(row=6, column=3, padx=2, pady=2, sticky='wens')

if __name__ == '__main__':
    win.mainloop()