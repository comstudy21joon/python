
data_list = [
    {
        "direction" : 'L',
        "angle" : 0,
        "length" : 200
    },
    {
        "direction" : 'L',
        "angle" : 90,
        "length" : 100
    },
    {
        "direction" : 'R',
        "angle" : 90,
        "length" : 50
    },
    {
        "direction" : 'R',
        "angle" : 90,
        "length" : 100
    },
    {
        "direction" : 'L',
        "angle" : 90,
        "length" : 200
    }
]

from turtle import Turtle

t = Turtle()
t.color("RED")
t.pensize(5)
t.shape("turtle")

def moveTurtle(i) :
    print(data_list[i])
    direction = data_list[i]['direction']
    angle = data_list[i]['angle']
    length = data_list[i]['length']

    t.left(angle) if direction == "L" else t.right(angle)
    t.forward(length)


for i in range(0,5) :
    moveTurtle(i)

input('Press any key to continue ...')
