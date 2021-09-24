from tkinter import Tk, PhotoImage, Label, Button

def changed(newImg) :
    imgLabel.configure(image = newImg, width=600, height=350)
    imgLabel.image=newImg

def img1() :
    newImg = PhotoImage(file="logo_python.png");
    changed(newImg)


def img2() :
    newImg = PhotoImage(file="logo_java.png");
    changed(newImg)


def img3() :
    newImg = PhotoImage(file="logo_nodejs.png");
    changed(newImg)


win = Tk()
win.geometry("600x400+100+100")

image = PhotoImage(file="logo_python.png");
imgLabel = Label(win, image=image, width=600, height=350)

btn_python = Button(win, text="Python", command=img1)
btn_JAVA = Button(win, text="JAVA", command=img2)
btn_Nodejs = Button(win, text="NodeJS", command=img3)


imgLabel.grid(row=0, column=0, columnspan=3)
btn_python.grid(row=1, column=0)
btn_JAVA.grid(row=1, column=1)
btn_Nodejs.grid(row=1, column=2)


if __name__ == '__main__':
    win.mainloop()