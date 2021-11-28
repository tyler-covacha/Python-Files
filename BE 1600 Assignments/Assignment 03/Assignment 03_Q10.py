my_dict = {'a':15 , 'c':35, 'b':10}

# print all keys
print("Keys:",end=" ")
for i,j in my_dict.items():
    print(i,end=' ')
print()

# print all values
print("Values:",end=" ")
for i,j in my_dict.items():
    print(j,end=' ')
print()

# print all keys and values pairs
for i,j in my_dict.items():
    print(i,j)
print()

# print keys and values pairs in order of key
print("Key-Value pairs- sorted by key")
L = []
for i,j in my_dict.items():
    L.append([i,j])
L.sort()
for i in L:
    print(i[0],i[1])
print()

# print keys and values in order of value
print("Key-Value pairs- sorted by value")
L = []
for i,j in my_dict.items():
    L.append([j,i])
L.sort()
for i in L:
    print(i[1],i[0])
