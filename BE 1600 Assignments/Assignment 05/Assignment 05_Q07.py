alpha = [[],[],[],[]]


print("part a")

for i in range(4):
    for j in range(3):
        alpha[i].append(0)
    for k in range(3):
        print(alpha[i][k], end=' ')
    print()

    
print("part b")

for i in range(1):
    for j in range(3):
        alpha[i][j] = 1
    for k in range(3):
        print(alpha[i][k], end=' ')
    print()
    
for i in range(1,4):
    for j in range(3):
        alpha[i][j] = 3
    for k in range(3):
        print(alpha[i][k], end=' ')
    print()


print("part c")

for i in range(3):
    x = 2
    for j in range(4):
        alpha[j][i] = x ** (i + 1)

for i in range(4):
    for k in range(3):
        print(alpha[i][k], end=' ')
    print()
    

