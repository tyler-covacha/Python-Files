# median function
def median(L):
    L.sort()        #sorts list from smallest to largest
    if len(L) % 2 != 0:
        i = len(L)//2
        return L[i]
    else:
        x = len(L)//2
        y = x - 1
        return (L[x] + L[y]) / 2
    
L = [7,5,9,2,1,5,8,-1,7]
print(median(L))
