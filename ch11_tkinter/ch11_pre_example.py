import turtle
import tkinter as tk

class App:
    def __init__(self, win):
        self.win = win
        self.win.title("Raw Turtle")
        self.canvas = tk.Canvas(win)
        self.canvas.config(width=600, height=200)
        self.canvas.pack(side=tk.LEFT)
        self.scr = turtle.TurtleScreen(self.canvas)
        self.button = tk.Button(self.win, text="Press me", command=self.press)
        self.button.pack()
        self.t = turtle.RawTurtle(self.scr, shape="turtle")
        self.t.speed(0);
        self.t.pensize(3)

    def action_turtle(self):
        y = 80
        x = -100
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        for i in range(40) :
            for j, color in enumerate(["red", "yellow", "green"]):
                self.t.color(color)
                self.t.forward(80)
            self.t.penup()
            y-=4
            self.t.goto(x,y)
            self.t.pendown()


    def press(self):
        self.action_turtle()


if __name__ == '__main__':
    win = tk.Tk()
    app = App(win)
    win.mainloop()