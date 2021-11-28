L = [1,5,2,1,1,6,3,1,5,5,5]
d = {}
for e in L:
    if e not in d:
        d[e] = 1
    else:
        d[e] = d[e] + 1
        
for i,j in d.items():
    print(i,j)
print()

v = list(d.values())
m = max(v)
for i in d.keys():
    if d[i] == m:
        print(i)
