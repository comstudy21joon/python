from tkinter import Tk, Label

x = 150
y = 100

def mouseEvtHandler(event) :
    global x,y
    x, y = (event.x, event.y)
    print("{}, {}".format(x, y))
    lbl.place(x=x, y=y)


def scroll(event) :
    global y
    #print(event.delta)
    if event.delta == -120 : # 업 스크롤
        y += 10
    if event.delta == 120 : # 다운 스크롤
        y -= 10
    lbl.place(x=x, y=y)


win = Tk()
win.geometry("300x200+100+100")

lbl = Label(win, text="자연인")
lbl.place(x=150, y=100)

win.bind("<B1-Motion>", mouseEvtHandler)
win.bind("<MouseWheel>", scroll)

if __name__ == '__main__':
    win.mainloop()