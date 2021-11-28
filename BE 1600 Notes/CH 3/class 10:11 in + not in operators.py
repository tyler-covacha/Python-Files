s = "Welcome to python"
x = "eyn"
counter = 0
counter2 = 0

for i in s:
    #print(s[i])
    #if s[i] in x:
    if i in x:
        counter += 1
    #elif s[i] not in x:
    elif i not in x:
        counter2 += 1

print(counter)
print(counter2)
