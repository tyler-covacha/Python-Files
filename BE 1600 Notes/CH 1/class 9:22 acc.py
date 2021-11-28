
def f(n):
    acc = 0
    for x in range(n + 1): #if f(4), then 1 + 2 + 3 + 4 = acc
        acc = acc + x
        print(acc)
    
f(100)

