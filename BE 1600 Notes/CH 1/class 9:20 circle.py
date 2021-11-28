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

import turtle
t = turtle.Turtle()
t.up()
t.backward(200)
t.left(90)
t.down()
circle(t,20)
circle(t,200)
