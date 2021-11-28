#Sentinal loop
s = -999
print("Enter numbers ended with -999")
acc = 0
x = int(input())
while x != s:
    acc = acc + x
    x = int(input())
print(acc)




import math

print("Enter the radius of the Circle")
r = int(input())
while r <= 0:
    print("radius of circle must be positive, Enter a number again")
    r = int(input())
print("Area of Circle = ",math.pi * r ** 2)
