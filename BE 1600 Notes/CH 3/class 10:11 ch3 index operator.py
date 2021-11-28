s = 'APPLE' #can use ' ' 
s2 = "Orange" #or " "
s3 = """ #starts
type anything here
""" #ends

#>>> print(s3)
# type anything here

#x = 45      can only store one int
#s = 'APPLE' stores multiple characters

#>>> s [0] #indexing operator
#'A'



#operator and method

#>>> s = "Apple"
#>>> len(s)             len() - length of list, string, dictionary, iterable data format
# 5

#>>> s[len(s)-1]
# 'e'

#>>> s[:]
#'Apple'

#>>> s[1:]
#'pple'

#>>> s[:4]
#'Appl'

#>>> s[1:3]
#'pp'



#>>> s = "Apple"
#>>> "Apple"+"Orange"
#'AppleOrange
#>>> s + "Orange"
#'ApppleOrange'



# indexing operator
#0 1 2 3 4 5
#h i   h i e
#-6 -5 -4 -3 -2 -1

#>>> s = "ABCDEF"
#>>> s[-1]
#'F'
#>>> s[5]
#'F'




# slicer 
#>>> s = "ABCDEF"
#>>> s[::2]
#'ACE'

#>>> s[::-1]
#'FEDCBA'




#Capital A to lowercase a
#>>> s = "Apple"
#>>> s2 = "a" + s[1:5]

#can't modify a string
#s[0] = "a"      cant do this



#>>> s1 = "ABC"
#>>> s2 = "DEF"
#>>> s1 + s2
#'ABCDEF'
#>>> s1 * 10
#'ABCABCABCABCABCABC'
