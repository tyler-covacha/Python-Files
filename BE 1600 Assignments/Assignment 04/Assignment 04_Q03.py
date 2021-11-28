f = open("thisFile.txt",'r')
L = []

for line in f:
    L.append(line)

f.close()

f2 = open("thatFile.txt",'w')
for i in range(0,12,2):
    f2.write(L[i])

f2.close()
