import turtle
t = turtle.Turtle()

x = 1

def line(t):
    t.forward(x)
    t.left(89)


for w in range(1000):
    t.color("green")
    line(t)
    x = x + 1
    t.color("Red")
    line(t)
    x = x + 1
    t.color("Blue")
    line(t)
    x = x + 1
    
