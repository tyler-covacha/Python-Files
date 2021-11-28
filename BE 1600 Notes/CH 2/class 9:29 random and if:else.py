import random
#random.random() prints a random number between 0-1
#random.randint(x,y) find a random number between x-y
#for i in range(10):
    #print(random.randint(5,10))
for i in range(5):
    a = random.randint(1,9)
    b = random.randint(1,9)
    print("What is",a,"+",b,"= ?")
    x = int(input())
    print(x)

    if x == a + b:
        print("Right")

    else:
        print("u suck")

