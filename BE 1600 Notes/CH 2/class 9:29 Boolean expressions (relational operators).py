#int float string bool
#relational operators == != < <= > >=

a = int(2)
b = int(6)
x = a > b
print(x)

#"A" < "a"
#true b/c ASCII A = 65, ASCII a = 97

#"ABC" < "ACD"
#reads from left to right of each side
#ie. A == A , B < C --> true

#true-false table for and
    #True and True --> True
    #True and False --> False
    #False and True --> False
    #False and False --> False

#true-false table for or
    #True or True --> True
    #True or False --> True
    #False or True --> True
    #False or False --> False

#x = 11
#x > 10 --> True
#x > 1 --> True
#x < 10 --> False
#(x > 1) and (x < 10) --> False
#(x > 1) or (x < 10) --> True

#can do:
    #True and True or False
    #reads from left to right

#not statements
    #not True --> False
    #not False --> True
    #not(5 < 2) --> True
