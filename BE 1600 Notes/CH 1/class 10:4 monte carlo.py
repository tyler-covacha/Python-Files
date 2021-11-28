import random
import math
inCircle = 0
z = 1000000

for i in range(z):
    x = random.random()
    y = random.random()
    d = math.sqrt(x ** 2 + y ** 2)

    if d <= 1:
        inCircle = inCircle + 1

print("points inside circle:", inCircle)
print(inCircle/z)
