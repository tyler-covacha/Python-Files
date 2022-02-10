# to access a pixel, must find it by row, then column

L = [[1,2],
     [3,4],
     [5,6]] # 3x2 dimension

# print the whole table
for r in range(len(L)):
    for c in range(len(L[r])):
        print(L[r][c],end=" ")
    print()
print()

# print a specific row
for i in range(len(L[1])):
    print(L[1][i], end=" ")
print()
print()

# print a specific column
for j in range(len(L)):
    print(L[j][0])
