import turtle
t = turtle.Turtle()

a = -1
b = 2
t.up() #starting position
t.goto(a,b)
t.down()
x = 1


def octo(t): #octagon
    t.forward(x)
    t.right(45)
for w in range (100): 
    for o in range(8):
        octo(t)
    a = a - 2
    b = b + 1
    t.up()
    t.goto(a,b)
    t.down()
    x = x + 1
