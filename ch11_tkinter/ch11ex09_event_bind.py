from tkinter import Tk, Label

x = 150
y = 100

def leftClick(event) :
    global x
    x -= 10;
    lbl.place(x=x, y=y)
    print("{}, {}".format(x, y))


def wheelClick(event) :
    global x
    x = event.x;
    lbl.place(x=x, y=y)
    print("{}, {}".format(x, y))


def rightClick(event):
    global x
    x += 10;
    lbl.place(x=x, y=y)
    print("{}, {}".format(x, y))


win = Tk()
win.geometry("300x200+100+100")

lbl = Label(win, text="자연인")
lbl.place(x=150, y=100)

win.bind("<Button-1>", leftClick)
win.bind("<Button-2>", wheelClick)
win.bind("<Button-3>", rightClick)

if __name__ == '__main__':
    win.mainloop()