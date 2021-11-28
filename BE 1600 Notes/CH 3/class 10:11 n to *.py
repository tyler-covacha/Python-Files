s = "Welcome to Python" #string
s2 = "" #empty string

for l in s:
    if l == "e":
        s2 = s2 + "*"
    else:
        s2 = s2 + l
    
print(s2)
