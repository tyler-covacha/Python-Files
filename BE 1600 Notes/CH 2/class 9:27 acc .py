#infinite series & infinite product expansions

#leibniz formula
#pi/4 = 1/1 - 1/3 + 1/5 - 1/7...

#wallis formula
#pi/2 = 2/1 * 2/3 * 4/3 *4/5 * 6/5 * 6/7

2 * 7 * 12 * 14 * 22 ..
acc = 1
num = 2
for x in range(10):
    acc = acc * num
    num = num + 5

print(acc)
    
