L = []
for i in range(10):
    x = float(input("Enter a number:"))
    L.append(x)
minimum = min(L)
print("Low:",minimum)
maximum = max(L)
print("High:",maximum)
total = 0
for x in range(len(L)):
    total += L[x]
print("Total:",total)
average = total / len(L)
print("Average:",average)
