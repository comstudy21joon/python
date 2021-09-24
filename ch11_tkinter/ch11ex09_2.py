from tkinter import *

win = Tk()
win.geometry("400x400+100+100")

def zoomin(event):
    print("zoom in")


def zoomout(event):
    print("zoom out")


win.bind("<Button-4>", zoomin)
win.bind("<Button-5>", zoomout)
win.focus_set()

if __name__ == '__main__':
    win.mainloop()