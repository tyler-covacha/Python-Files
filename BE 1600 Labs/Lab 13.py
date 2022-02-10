def list_function(L):
    
    print("2D list")
    for row in L:
        
        for col in row:          
            print("{0:>3d}".format(col),end='')
        print()

    col_L = []
    for col in range(3):
        temp_col = []
        for row in range(4):
            temp_col.append(L[row][col])
        col_L.append(temp_col)

    neg_L = []
    print("Number of odd negative values")
    for i in range(3):
        temp_neg = 0
        for col in col_L[i]:
            if col < 0:
                if col % 2 != 0:
                    temp_neg += 1
        neg_L.append(temp_neg)

    return neg_L

list_2D = [[-2,3,-5],[-8,4,-6],[9,-3,77],[11,-2,9]]
L = list_function(list_2D)
for i in range(3):
    print("Col",i + 1,":",L[i])
    
