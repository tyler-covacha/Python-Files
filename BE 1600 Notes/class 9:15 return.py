def read():
    n1 = input("enter a number")
    n1 = int(n1)
    return n1

def add():
    x1 = read()
    x2 = read()
    results = x1 + x2
    return results

results = add()
print(results)

