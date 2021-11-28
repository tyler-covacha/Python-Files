# min of list function
def min(L):
    cm = L[0]
    for i in range(1,len(L)):
        if L[i] < cm:
            cm = L[i]
        
    return cm;

L = [7,5,9,2,1,5,8,7]
print(min(L))
