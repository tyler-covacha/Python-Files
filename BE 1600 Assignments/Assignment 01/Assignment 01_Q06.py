
monthly = float(input("Enter the total sales for the month"))
print("Monthly sales: $", monthly)

state = float(monthly * (4 / 100))
print("State tax: $", state)

county = float(monthly * (2 / 100))
print("County tax: $", county)

total = print("Total tax: $", state + county)
