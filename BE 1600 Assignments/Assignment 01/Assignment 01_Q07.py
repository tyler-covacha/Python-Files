wallspace = float(input("Enter wall space in square feet:"))
paintprice = float(input("Enter paint price per gallon:"))

paint = (wallspace / 115) + 1
paint = int(paint)
print("Gallons of paint:",paint)

hours = int(paint * 8)
print("Hours of labor:", hours)

paintprice = float(paintprice * paint)
print("Paint charges: $", paintprice)

laborprice = hours * 20
print("Labor charges: $", laborprice)

total = paintprice + laborprice
print("Total cost: $",total)


