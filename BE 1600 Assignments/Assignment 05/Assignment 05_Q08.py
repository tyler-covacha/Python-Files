years = int(input("Enter the number of years: "))
total_rainfall = 0

for year in range(1,years + 1):
    print("For year ",year,':')
    
    for month in range(1,13):
        print("Enter the rainfall amount for the month",month,end='')
        rainfall = float(input(': '))
        total_rainfall += rainfall

months = years * 12
average_rainfall = total_rainfall / months

print("For ",months,"months")
print("Total rainfall: ",total_rainfall,"inches")
print('Average monthly rainfall: {0:.2f} inches'.format(average_rainfall))

    






