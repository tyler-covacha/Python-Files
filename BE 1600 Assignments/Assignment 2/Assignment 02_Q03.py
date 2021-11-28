num = 1
den = 30
total = 0

for i in range(den):
    fraction = (num/den)
    total = total + fraction
    num = num + 1
    den = den - 1
    
print(total)
    
