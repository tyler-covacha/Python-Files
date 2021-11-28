d = {'j':3,'b':1,'z':7,'w':4}
keys = list(d.keys())
keys.sort()
for i,j in d.items():
    print(i,j)

print()
for k in keys:
    print(k,d[k])

L = []
for i,j in d.items():
    L.append([j,i])
L.sort()
print(L)
print()
for e in L:
    print(e[1],e[0])

    
