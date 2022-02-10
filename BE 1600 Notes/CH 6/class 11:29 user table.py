import random

row = int(input("Enter number of rows "))
col = int(input("Enter number of columns "))

print("Enter ",row * col, "values")
L = []

# for every row
for r in range(row):
    temp = []

    # add every column in row into temp list and add to L list at the end
    for c in range(col):
        x = random.randint(0,9)
        #x = int(input())
        temp.append(x)
    L.append(temp)

# prints L as a row and column table
for r in range(len(L)):
    for c in range(len(L[r])):
        print(L[r][c],end=" ")
    print()


        
