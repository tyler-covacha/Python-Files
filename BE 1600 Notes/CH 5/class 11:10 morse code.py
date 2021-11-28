encoding = {}
decoding = {}
f = open("morse.txt",'r')
for line in f:
    line = line.split()
    encoding[line[0]] = line[1]
    decoding[line[1]] = line[0]
f.close()
print(encoding)
print(decoding)
