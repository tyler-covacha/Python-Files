#list operators * + [:] in not in del
# list methods append, osrt
#split
#min, max, average, median, and mode
#Tuples and Mutable list

#######################################################

# operators in lists
#>>> L2 = [0]*3
#>>> L2
# [0, 0, 0]




# slicing lists
#>>> L = [7, 5, 9, 2, 1, 5, 8, 7, 10]
#>>> L[:2]
# [7, 5]




# deleting elements in a list
#>>> L = [7, 5, 9, 2, 1, 5, 8, 7, 10]
#>>> del L[len(L)-1]
# [7, 5, 9, 2, 1, 5, 8, 7]



# lists are mutable (as opposed to strings which are not modifiable)
#>>> L = [7, 5, 9, 2, 1, 5, 8, 7, 10]
#>>> L[0] = 8
#>>> L
# [8, 5, 9, 2, 1, 5, 8, 7, 10]



# minimum and maximum of lists
#>>> L = [7, 5, 9, 2, 1, 5, 8, 7, 10]
#>>> min(L)
# 1
#>>> max(L)
# 10



# median –– list must be sorted to find median
#>>> L = [3,5,8,10]
#>>> index = len(L)// 2
#>>> index
# 2
#>>> (L[index] + L[index-1])/ 2
# 6.5
#
#
#
#>>> L = [1,2,3,4,5]
#>>> i = len(L)// 2
#>>> L[i]



# shallow copy vs deep copy
    # shallow copies modify original list
#>>> L = [1,2,3]
#>>> L2 = L
#>>> L2.append(100)
#>>> L2
# [1,2,3,100]
#>>> L
# [1,2,3,100]
    # deep copy
#>>> L = [1,2,3]
#>>> L3 = L[:]
#>>> L.append(100)
#>>> L
# [1,2,3,100]
#>>> L3
# [1,2,3]



# min of list function
def min(L):
    cm = L[0]
    for i in range(1,len(L)):
        if L[i] < cm:
            cm = L[i]
        
    return cm;

L = [7,5,9,2,1,5,8,7]
print(min(L))



# average function
def average(L):
    acc = 0
    for e in L:
        acc = acc + e
    return acc /len(L)

L = [7,5,9,2,1,5,8,7]
print(average(L))



# search function
def search(L, key):
    if key in L:
        return True
    else:
        return False

L = [7,5,9,2,1,5,8,7]
key = 9 
x = search(L, 9)
if x == True:
    print(key,"is in list L")
else: print(key,"is not in list L")



# median function
def median(L):
    L.sort()        #sorts list smallest to largest
    if len(L) % 2 != 0:
        i = len(L)//2
        return L[i]
    else:
        x = len(L)//2
        y = x - 1
        return (L[x] + L[y]) / 2
    
L = [7,5,9,2,1,5,8,-1,7]
print(median(L))



# 
