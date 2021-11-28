def draw(myTurtle,sideLength,numside):
    delta = 360 // numside
    for i in range(numside): #number of sides
            myTurtle.forward(sideLength)
            myTurtle.left(delta)
import math
p = math.pi
def circle(myTurtle,radius):
    c = 2 * p * radius
    sideLength = c / 360
    drawpoly(myTurtle,sidelength,360)
            
import turtle
t = turtle.Turtle()
t.up()
t.goto(-50 , -50)
t.down()
for i in range(3,100,2): #[ 3,5,7] #range(1,8) starts from 1, ends at 7
        #range(x,y,z) z is how much it skips ; #range(x,y) x and y are called arguments
    draw(t,125,i) #(t,100) t is myTurtle and 100 is sideLength
    print(i)
