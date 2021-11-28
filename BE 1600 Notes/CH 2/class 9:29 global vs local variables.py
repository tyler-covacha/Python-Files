#table

def addNumbers():
    acc2 = 5 #local variable - can be accessed in the function only
    #print(acc) #prints local variable
    return acc2 #allows local variable to be used outside of function
#               but cannot be used as a global variable

acc = 10 #global variable - outside of function
addNumbers()
print(acc2) #print global variable
