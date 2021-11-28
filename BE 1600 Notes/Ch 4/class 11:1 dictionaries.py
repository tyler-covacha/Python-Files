s = "" # string
L = [] # list
d = {} # dictionary

d = {"Jack": 35, "Sarah": 25, "Sam": 25}

# dictionaries don't have indexes (cannot call "Jack": 35 by d[0]
                                #  have to do d["Jack"]

# add element to dictionary
d["John"] = 22
print(d)
print("")

# printing an element from dictionary
print(d["John"])
print("")

# delete element to dictionary
del d["Jack"]
print(d)
print("")

# assigning values to elements
d["Sam"] = 100
print(d)
print("")

# incrementing values of elements
d["John"] = d["John"] + 1
print(d["John"])
print("")

# creating list from string
print(list("apple"))
print("")

# extracting all keys
print(d.keys())

# creating list from dictionary keys
print(list(d.keys()))
print("")

# extracting values of keys
print(d.values())

# creating list from dictionary values
print(list(d.values()))
print("")

# extacting keys and their values
print(d.items())

# creating list of keys and their values
print(list(d.items()))
print("")

# searching items in dictionaries
print("Jack" in d)
print("Jack" not in d)
print("Sarah" in d)
print("")

# finding a key that doesn't exist in a dictionary
print(d.get("Jack"))
print(d.get("Jack","Jack is not in d"))
