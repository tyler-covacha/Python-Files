d = {'Z':4,'B':1,'C':5}

''' prints key and value in order of key '''
keys = list(d.keys())
keys.sort()
for key in keys:
    print(key,d[key])

''' prints key and value in order of value '''
items = list(d.items())
L = []

# key, value -> value, key
for e in items:
    L.append((e[1],e[0]))
L.sort()

for e in L:
    print(e[1],e[0])

