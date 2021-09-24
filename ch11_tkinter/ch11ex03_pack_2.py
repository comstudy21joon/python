from tkinter import Tk, Label, Button

win = Tk()
win.geometry("600x400+100+100")

top_label = Label(win, text="top", background="Cyan")
top_label.pack(side="top", fill="x")

left_label = Label(win, text="left")
left_label.pack(side="left")

right_label = Label(win, text="right")
right_label.pack(side="right")

bottom_label = Label(win, text="bottom")
bottom_label.pack(side="bottom")

btn = Button(win, text="btn")
btn.pack(side="bottom", anchor="e")


if __name__ == '__main__':
    win.mainloop()