def double_list(L):

    # empty list: L2
    L2 = []

    # loop for each element in list L
    for i in L:

        # element added to L2, twice
        for e in range(2):
            L2.append(i)
    
    print("double list:",L2)

List = ['how','are','you?']
print("original list:",List)
double_list(List)
