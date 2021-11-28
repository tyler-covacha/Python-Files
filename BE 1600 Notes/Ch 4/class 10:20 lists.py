# lists use brackets []
#L = []
#print(L) >>> []



# lists can have lists
L = [2,3,4.4, True,"abcd",[2,3,4]]
#print(L) >>> [2,3,4.4, True,"abcd",[2,3,4]]



for i in range(len(L)):
    print(L[i])

for i in L:
    print(i)

# can replace statements in a list
#L[5] = 100
#print(L) >>> [2, 3, 4.4, True, 100, [2,3,4]]

# can add statements to end of list
#L.append(22)
#print(L) >>> [2,3,4.4, True,100,[2,3,4], 22]

