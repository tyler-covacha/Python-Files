def circle1():
    for i in range(750):
        t.forward(.5)
        t.left(.5)

def circle2():
    for i in range(750):
        t.forward(.5)
        t.right(.5)

def up():
    t.up()
    t.goto(0,-100)
    t.down()

import math
p = math.pi

def drawpoly(myTurtle,sidelength,numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        myTurtle.forward(sidelength)
        myTurtle.right(turnAngle)
    
def circle(myTurtle,radius):
    c = 2 * p * radius
    sidelength = c / 360
    drawpoly(myTurtle,sidelength,360)

def halfcircle(myTurtle,radius):
    c = 2 * p * radius
    c = float(c)
    sidelength = c / 360
    drawpoly(myTurtle,sidelength,360)

def halfcircle1():
    for i in range(180):
        t.forward(1)
        t.right(1)
    
   

import turtle
t = turtle.Turtle()
t.color('red')
t.speed(9999)
t.left(90)
t.up()
t.goto(0,-100)
t.down()
circle(t,50)
t.up()
t.goto(-100,-100)
t.down()
circle(t,50)

t.up()
t.goto(-50,-50)
t.down()
t.forward(160)
halfcircle1()
t.forward(160)




