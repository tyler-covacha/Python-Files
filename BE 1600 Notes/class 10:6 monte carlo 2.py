import turtle
import random
import math
p = math.pi
pi = math.pi

t = turtle.Turtle()
s = turtle.Screen()
s.setworldcoordinates(-2,-2,2,2)

def cross():
    t.up()
    t.goto(0,1)
    t.down()
    t.right(90)
    t.forward(2)
    t.up()
    t.goto(-1,0)
    t.down()
    t.left(90)
    t.forward(2)
    

def dart():
    for i in range(10000):
        x = random.random()
        y = random.random()
        d = x ** 2 + y ** 2
        if d <= 1:
            t.color('blue')
        else:
            t.color('red')
        t.up()
        t.goto(x,y)
        t.down()
        t.dot()
        
def drawpoly(myTurtle,sidelength,numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        myTurtle.forward(sidelength)
        myTurtle.right(turnAngle)
    
def circle(myTurtle,radius):
    t.up()
    t.goto(0,1)
    t.down()
    c = 2 * pi * radius
    sidelength = c / 360
    drawpoly(myTurtle,sidelength,360)

def square(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    for i in range(4):
        t.right(90)
        t.forward(2)



cross()
square(1,1)
circle(t,1)
dart()



