import math

def inCircle(xpoint,ypoint,radius):
    distance = math.sqrt(xpoint ** 2 + ypoint ** 2)
    if distance < radius:
        print("Point (",xpoint,",",ypoint,") is in circle with radius",radius)
    else:
        print("Point (",xpoint,",",ypoint,") is not in circle with radius",radius)

#point not in circle
inCircle(10,-10,8)

#point in circle
inCircle(5,-5,8)
