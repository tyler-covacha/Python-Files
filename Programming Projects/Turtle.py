import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.setworldcoordinates(-10,-10,10,10)

def wasd():
    print("move (wasd), x to quit, press enter every time")
    while True:
        y = input("")
        if y == 'w':
            t.forward(1)
        elif y == 'a':
            t.left(90)
        elif y == 'd':
            t.right(90)
        elif y == 's':
            t.backward(1)
        if y == 'x':
            break

wasd()
