# search function
def search(L, key):
    if key in L:
        return True
    else:
        return False

L = [7,5,9,2,1,5,8,7]
key = 9
x = search(L, key)
if x == True:
    print(key,"is in list L")
else: print(key,"is not in list L")
