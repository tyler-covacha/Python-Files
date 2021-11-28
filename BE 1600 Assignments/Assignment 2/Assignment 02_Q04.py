import random
evenCounter = 0
oddCounter = 0

for i in range(100):
    r = random.randint(1,100)
    if r % 2 == 0:
        evenCounter = evenCounter + 1
    else:
        oddCounter = oddCounter + 1

print("Out of 100 random numbers, ",oddCounter," were odd, and ",evenCounter,"were even.")

        
