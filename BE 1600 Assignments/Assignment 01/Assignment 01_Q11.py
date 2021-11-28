def sum(x,y):
    acc = 0
    for i in range(x,y + 1):
        print(i,end=" ")
        acc = acc + i
    print("\nsum of numbers:", acc)
    
A = 5
B = 10
sum(A,B)
