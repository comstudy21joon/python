'''
class Washer :
    def __init__(self, maker, brand, weight) :
        self.maker = maker
        self.brand = brand
        self.weight = weight

    def washing(self) :
        print("{} {} 세탁기가 {}킬로그램의 빨래를 합니다.".format(self.maker, self.brand, self.weight))

washer = Washer("LG", "트롬", 65)
washer.washing()
'''
from pycparser.c_ast import Constant

'''
class Music :
    def __init__(self, track, title, singer):
        self.track = track
        self.title = title
        self.singer = singer

    def play(self):
        print("%d번 트랙 %s의 %s 실행중입니다." %(self.track, self.title, self.singer))


music = Music(1, "Festival", "엄정화")
music.play()
'''


'''
class Point :
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def set_point(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def show_point(self):
        print('x=%d, y=%d' %(self.x, self.y))


p1 = Point(10, 20)
p1.show_point();

p1.set_point(100, 200)
print(p1.get_x(), p1.get_y())
'''




'''
class Music :
    def __init__(self, track, title, singer):
        self.track = track
        self.title = title
        self.singer = singer

    def play(self):
        print("%d번 트랙 %s의 %s 실행중입니다." %(self.track, self.singer, self.title))


class MusicPlayer :
    def __init__(self):
        self.track_num = 1;
        self.music_list = [];

    def append(self, music):
        self.music_list.append(music)

    def input(self):
        while True :
            track = self.track_num
            self.track_num += 1
            title = input('곡목 입력 >> ')
            if title == '그만' :
                print('곡 추가 기능을 마칩니다!')
                break
            singer = input('가수 입력 >> ')
            music = Music(track, title, singer)
            self.append(music)

    def delete(self, index):
        try :
            m = self.music_list[index-1]
            print("%d번 트랙 %s의 %s 삭제" %(m.track, m.singer, m.title))
            del self.music_list[index-1]
        except :
            print('삭제 할 음악이 없습니다!')

    def play_all(self):
        for music in self.music_list :
            music.play()


mp = MusicPlayer()
while True :
    print("::: Music Player :::")
    no = int(input("(1)추가 (2)제거 (3)전곡 실행 (4)종료 >> "))
    if no == 1 :
        print("새 노래를 계속 입력 하세요. (종료는 '그만') >>")
        mp.input()
    elif no == 2 :
        idx = int(input('삭제 할 번호 입력 >> '))
        mp.delete(idx)
    elif no == 3 :
        mp.play_all()
    elif no == 4 :
        print("뮤직 플레이어 종료!")
        break
'''



class Point :
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def set_point(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def show_point(self):
        print('x=%d, y=%d' %(self.x, self.y), end="")



class Point3D(Point) :
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def set_point(self, x, y, z):
        super().set_point(x, y)
        self.z = z

    def get_z(self):
        return self.z

    def show_point(self):
        super().show_point()
        print(', z=%d' %self.z)


p3d = Point3D(10,20,30)
p3d.show_point()
p3d.set_point(100,200,300)
print(p3d.get_x(), p3d.get_y(), p3d.get_z())