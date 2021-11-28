def KiloToMiles(kilo):
    miles = kilo * 0.6214
    return miles

kilo = float(input("Enter the distance in kilometers:"))
miles = KiloToMiles(kilo)
print("The converson of", kilo , "kilometers to miles is ", miles, "miles.")
