#pi/2 = 2/1 * 2/3 * 4/3 *4/5 * 6/5 * 6/7
acc = 1
num = 2
for i in range(100):
    left = num/ (num-1)
   #print(left) #Most people check their results by printing local variables
    right = num/ (num+1)
    #print(right) #Afterwards, they add # before the print for future reference/use

    acc = acc * left * right

    num = num + 2

print(acc)


