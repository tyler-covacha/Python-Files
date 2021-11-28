import csv
f = open("earthquake.csv",'r')
f2 = csv.reader(f)
L = list(f2)
print(L[0])
f.close()
