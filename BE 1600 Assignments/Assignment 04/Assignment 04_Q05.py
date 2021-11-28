f = open("books.txt")

L =  []

for line in f:
    line = line.split(',')
    line0 = line[0].strip()
    line1 = line[1].strip()
    L.append([line1,line0])

d = {}

for i,j in L:   
    if "'" in j:
        j = '"{0}"'.format(j)
    else:
        j = "'{0}'".format(j)       
    if i not in d:
        d[i] = j
    else:
        d[i] = d[i] + ', ' + j

for k,l in d.items():
    print("{0:s} [{1}]".format(k,l))


