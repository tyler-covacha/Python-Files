f = open("filename.txt",'r')
cities = []
rain = []
for line in f:
    L = line.split()
    print(L)
    cities.append(L[0])
    rain.append(int(L[1]))
print(cities)
print(rain)
x = min(rain)
print('x:',x)
y = max(rain)
print('y:',y)
f.close()

f2 = open("filenameValues.txt",'w')
f2.write('Min: ' + str(x) + ', Max: ' + str(y))
f2.close()

