import random

name_file = input("Enter the name of the file to which result should be written: ")
number_length = int(input("Enter the number of random numbers to be written to the file: "))

f = open(name_file,'w')

for i in range(number_length):
    f.write(str(random.randint(1,100)) + '\n')
    
f.close()
