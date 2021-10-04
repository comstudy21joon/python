import json
from socket import * #소켓 라이브러리 임포트

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
        self.t.pensize(3)

        self.client = socket(AF_INET, SOCK_STREAM)  # 소켓 생성
        self.client.connect(('127.0.0.1', 8088))  # ip와 포트번호를 맞게 넣어준다.

        print('연결 확인 됐습니다.')  # 연결됨을 확인하는 출력문


    def move(self):
        data = self.client.recv(1024)  # 데이터를 받을 준비
        #print('받은 데이터 : ', data.decode('utf-8'))  # 데이터를 받는다.
        obj = json.loads(data.decode('utf-8'))
        #print('받은 데이터 : ', obj)  # 데이터를 받는다.
        angle = obj['angle']
        direction = obj['direction']
        self.t.left(angle) if  direction=='L' else self.t.right(angle)
        self.t.forward(obj['length'])


    def press(self):
        self.client.send('I am a client2'.encode('utf-8'))  # 연결이 되었음을 서버에 알려준다.
        print('서버로 메시지를 전송했습니다.')  # 데이터를 전송함을 알려주는 출력문
        self.move()


if __name__ == '__main__':
    win = tk.Tk()
    app = App(win)
    win.mainloop()