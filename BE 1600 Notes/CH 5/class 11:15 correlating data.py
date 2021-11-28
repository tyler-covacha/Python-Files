import statistics
L1 = [3,4,5,6,7,8]
L2 = [4,5,2,1,9,8]
L1mean = statistics.mean(L1)
L2mean = statistics.mean(L2)
L1std = statistics.stdev(L1)
L2std = statistics.stdev(L2)
acc = 0
for i in range(len(L1)):
    acc = acc + (L1[i] - L1mean) * (L2[i] - L2mean)
corr = acc / ((len(L2) - 1) * L1std * L2std)
print(corr)
