fruit = "Apple"
price = 0.50

"{0}{1}{2}".format(fruit,price,4.456)

# s -> string       {} are string by default
# f -> float
# d -> decimal integer
# <10.1f -> 10 spaces after, float up to 1 value
# % -> percentage of decimal
# < -> starting from right side


>>> "{0:10s}{1:8f}{2}".format(fruit,price,4.456)
'Apple     0.5000004.456'

>>> "{0:10s}{1:<10f}{2}".format(fruit,price,4.456)
'Apple     0.500000  4.456'

>>> "{0:10s}{1:<10.1f}{2}".format(fruit,price,4.456)
'Apple     0.5       4.456'

>>> "{0:10s}{1:<10.1%}{2}".format(fruit,price,4.456)
'Apple     50.0%     4.456'

>>> "{0:10s}{1:<10.0%}{2}".format(fruit,price,4.456)
'Apple     50%       4.456'
