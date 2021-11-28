import string
alphabet = string.ascii_uppercase

'''histogram function'''
def histogram(user):

    # capitalizes letter of string user
    user = user.upper()

    # list of str(user) and sorts
    user = list(user)
    user.sort()

    # create empty list
    histo_list = []

    # loop of the length of list user
    for i in range(len(user)):

        # if user[i] is  an alphabet character, will be added to list histo_list
        if user[i] in alphabet:
            histo_list.append(user[i])

    
    # creates dictionary for each letter
    histo_dict = {}

    # for loop of each element in list histo_list
    for i in histo_list:

        # if element not in histo_dict, key created
        if i not in histo_dict:
            histo_dict[i] = 1

        # if element in histo_dict, value of that key += 1
        else:
            histo_dict[i] += 1

    # loop, each line prints letter and stars
    for i,j in histo_dict.items():
        print(i, '* ' * j)

#user_string = 'to be or not to be'
user_string = input()
print(user_string)
print()
histogram(user_string)
