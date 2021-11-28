import turtle
t = turtle.Turtle()

def drawSquare():
    x = -100
    y = 100
    a = 200
    for s in range(10):
        t.up()
        t.goto(x,y)
        t.down()
        x = x + 5
        y = y - 5
        for i in range(4):
            t.forward(a)
            t.right(90)
        a = a - 10

drawSquare()

