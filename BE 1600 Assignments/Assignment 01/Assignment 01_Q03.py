import math
pi = math.pi
def sphere_volume():
    volume = (4 / 3) * pi * r ** 3
    return volume

r = float(input("Enter the radius of a sphere:"))

sphere = sphere_volume()
print(sphere)
        
