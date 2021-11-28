import turtle
t = turtle.Turtle()

t.up()
t.goto(-200,200)
t.down()

def move(t):
    t.up()
    t.forward(150)
    t.down()

def reset(t):
    t.up()
    t.right(180)
    t.forward(450)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.down()
    

def draw(t):
    t.forward(100)
    t.right(144)

for e in range(3):
    for u in range(3):
        for x in range(5):
            draw(t)
        move(t)
    reset(t)



