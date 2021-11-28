f= open("tempconv.txt",'w')
f.write("{0:12s}{1:12s}".format('Fahrenheit','Celsius') + '\n')

for fahrenheit in range(-10,11):
    celsius = (fahrenheit - 32) * (5 / 9)
    f.write("{0:<12.2f}{1:<12.2f}".format(fahrenheit,celsius) + '\n')
    
f.close()


