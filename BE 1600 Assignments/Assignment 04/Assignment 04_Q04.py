import string

file_name = input("enter file name ")
print("{0:s}{1:>9s}".format('letter','count'))

alphabet = string.ascii_lowercase
d = {}

for letter in alphabet:
    d[letter] = 0

f = open(file_name,'r')

for line in f:
    for letter in line:
        if letter in d:
            d[letter] += 1
            
L = list(d.items())
L.sort()

for i,j in L:
    print("{0:<10}{1:.0f}".format(i,j))

