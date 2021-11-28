#alphabet: abcdefghijklmnopqrstuvwxyz
#     key: qwertyuiopasdfghjklzxcvbnm

# abc --> qwe

import string

def sub(astring):
    alphabet = string.ascii_lowercase
    key = "qwertyuiopasdfghjklzxcvbnm"
    newString = ""

    for e in astring:
        i = alphabet.find(e)
        newString = newString + key[i]
    return newString

print(sub("hello"))
