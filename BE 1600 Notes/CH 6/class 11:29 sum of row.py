L = [[1,2,3],
     [4,5,6],
     [7,8,9]]

# sum of values in row
for r in range(len(L)):
    acc = 0
    for c in range(len(L[r])):
        acc = acc + L[r][c]
    print(acc)

# sum of values in colum
for c in range(len(L[0])):
    acc = 0
    for r in range(len(L)):
        acc = acc + L[r][c]
    print(acc)
