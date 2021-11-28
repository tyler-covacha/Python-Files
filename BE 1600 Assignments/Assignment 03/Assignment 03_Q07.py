string = input("Enter a string: ")
L = list(string)
d = {}

''' character counter '''

# for loop for each character in list L
for i in L:

    # if character has not been added to dictionary d, character index created
    if i not in d:
        d[i] = 1

    # if character in dictionary d, value of index added by 1
    else:
        d[i] = d[i] + 1
        
maxk = 0
maxv = 0       
for i,j in d.items():
    if j > maxv:
        maxk,maxv = i,j
        
for e in d.keys():
    if d[e] == maxv:
        print("The character that appears most frequently in the string is",maxk.upper())
