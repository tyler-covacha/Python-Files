import random

def three_heads():
    head_counter = int(0)
    while head_counter < 3:
        r = random.randint(0,1)
        if r == 0:
            print('H',end=" ")
            head_counter += 1
        elif r == 1:
            print('T',end=" ")
            head_counter = int(0)
    print()
    print("Three heads in a row!")

three_heads()
    
        
    
