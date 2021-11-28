#one-way, two-way, multi-way

# % finds the remainder after dividing ie.) 7 / 2 = 3 R 1
# ie.) 7 / 2 = 3 R 1 | 7 % 2 = 1

#one-way - one thing or nothing
a = 2

if a % 2 == 0:
   print("Even")

print("Odd")



#two-way - one thing or another thing
r = float(input("Enter radius of circle"))

if r < 0: 
    print("invalid input")
else:
    print(3.14 * r ** 2)

print("after if statement")



#multi-way - multiple things
if r == 0:
    print("0")
elif r % 2 == 1:
    print("Odd")
else:
    print("Even")






