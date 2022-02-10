
print("first nested loop")
print()
for i in range(1,8):
    L = ''
    for j in range(i):
        L += '*'
    print(L)
print()

print("second nested loop")
print()
for i in range(7,0,-1):
    L = ''
    for j in range(i):
        L += '*'
    print(L)

