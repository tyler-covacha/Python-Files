import random

def dice_sum():
    desired_sum = int(7)
    r_total = int(0)
    while r_total != desired_sum:
        r1 = random.randint(1,6)
        r2 = random.randint(1,6)
        r_total = r1 + r2
        print(r1,'and',r2,'=',r_total)

dice_sum()
    
        
