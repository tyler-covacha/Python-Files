''' open("data.txt",'r')
L = [[1.5, 2.3], [2.1, 2.8]]
3.0 2.4
1.7 2.9
0.9 1.1
2.2 1.1
2.7 3.1 '''

for point in range(8):
    for point in range(8):
        

import math
def distance(p1, p2):
    d = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    return d

p1 = [1.5, 2.6]
p2 = [2.5, 3.6]
print(distance(p1,p2))



L = [1,2,3,4,5,6,7,8]
for i in range(1,9):
    for j in range(1,9):
        print(str(i) + " ", str(j), end= " ")
    print()
