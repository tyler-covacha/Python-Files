import string
import random

def removeChar(string,idx):
    return string[:idx] + string[idx+1:]

def keyGen():
    alphabet = string.ascii_lowercase
    key = ""
    for i in range(26):
        index = random.randint(0,25-i)
        key += alphabet[index]
        alphabet = removeChar(alphabet,index)
    return key

print(keyGen())

