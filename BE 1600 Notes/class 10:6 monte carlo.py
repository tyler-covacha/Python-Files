import random
import math

def MonteCarlo(n):
    counter = 0
    for i in range (n):
        x = random.random()
        y = random.random()
        d = math.sqrt(x**2 + y**2)
        if d <= 1:
            counter = counter + 1
        #print(x,y,d)
    pi = (counter/n) * 4
    return pi

print(MonteCarlo(1000000))

    
    
