def remove_duplicates(L):
    '''removes duplicate elements'''
    d = {}

    # create dictionary of how much an element shows up in list
    for i in L:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    # finds out if an element shows up more than once
    for i,j in d.items():

        # dictionary of those elements will now = 1
        if j > 1:
            d[i] = 1

    # make new list without duplicates       
    L = []
    for i in d:
        L.append(i)
        
    return L


L = ['be','is','be','not','or','question','that','the','to','to']
L.sort()
print('original list:',L)
print('list after removing duplicates:',remove_duplicates(L))
