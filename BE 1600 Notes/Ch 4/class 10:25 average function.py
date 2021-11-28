# average function
def average(L):
    acc = 0
    for e in L:
        acc = acc + e
    return acc /len(L)

L = [7,5,9,2,1,5,8,7]
print(average(L))
