#pi/4 = 1/1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 ...

acc = 1
num = -1
den = 3
for o in range(100000):
    acc = acc + (((-1) ** o) * num) / den
    den = den + 2

#acc = acc * 4 # this row tests if acc = pi | note, leibniz is pi/4
print(acc)
