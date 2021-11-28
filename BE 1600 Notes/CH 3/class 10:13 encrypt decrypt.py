#encrypt
e = "To be or not to be"
even = ""
odd = ""
for i in range(len(e)):
    if i % 2 == 0:
        even += e[i]
    else:
        odd += e[i]
secret = odd + even
print(secret)



#decrypt
d = secret
m = len(d)//2
odd = d[:m]
even = d[m:]
newString = ""
for i in range(len(odd)):
    newString += even[i]
    newString += odd[i]
if (len(even) > len(odd)):
    newString += even[-1]
print(newString)



#decrypt string length odd
##  ABCDE
##  even = ACE
##  odd = BD
##  BDACE
d = "BDACE"
m = len(d)//2
odd = d[:m]
even = d[m:]
newString = ""
for i in range(len(odd)):
    newString += even[i]
    newString += odd[i]
newString += even[-1]
print(newString)
