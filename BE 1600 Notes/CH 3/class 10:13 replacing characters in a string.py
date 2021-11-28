s = "JKLMNOPqxyz"
r = "mna"
newString = ""
s2 = s.lower()      #converts characters to lowercase
for e in s2:
    if e not in r:
        newString += e
        else:
            newString = newString + "8"
print(newString)
        
