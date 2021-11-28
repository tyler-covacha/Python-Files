f = open("filename.txt",'r')
f2 = open("out_file.txt",'w')

for line in f:
    L = line.split()
    x = float(L[1])
    print(L[0], x)

    L2 = [L[0],x * 2.54]
    s = "{0[0]:18s}{0[1]:<.2f}".format(L2)

    f2.write(s + '\n')
f.close()
f2.close()
    
