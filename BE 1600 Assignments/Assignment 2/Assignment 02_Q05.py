def areaRectangle(l1,w1,l2,w2):
    AreaA = l1 * w1
    print("Area A: ",AreaA)
    AreaB = l2 * w2
    print("Area B: ",AreaB)
    if AreaA > AreaB:
        print("Area A is greater than Area B")
    elif AreaA < AreaB:
        print("Area B is greater than Area A")
    else:
        print("Area A is equal to Area B")

#Sample output for rectangles A = 3 x 4 and B = 5 x 6
areaRectangle(3,4,5,6)

#Sample output for rectangles A = 3 x 4 and B = 4 x 3
areaRectangle(3,4,4,3)
