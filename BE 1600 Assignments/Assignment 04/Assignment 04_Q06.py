again = ''
while again != 'n':
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    print("The sum of the numbers you entered is",float(number1+number2))
    again = input("Do you want to do that again? (y/n): ")
