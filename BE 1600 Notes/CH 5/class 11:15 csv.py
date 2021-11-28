import csv
f = open("earthquake.csv",'r')
f2 = csv.reader(f)
titles = next(f2)
print(titles)
i = 0
while i != len(titles) and titles[i] != "Mag":
    i = i + 1
print(i)

L = []
for e in f2:
    L.append(float(e[i]))
L.sort()

d = {}
for e in L:
    if e not in d:
        d[e] = 1
    else:
        d[e] = d[e] + 1

print("{0:8s}{1:8s}".format("Items", "frequency"))
for k,v in d.items():
    if k > k + 0.5:
        k += 1
    print("{0:<8.1f}{1:<8.0f}".format(k, v))
