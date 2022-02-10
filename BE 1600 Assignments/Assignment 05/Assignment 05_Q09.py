def averageHigh(high):
    total = 0
    for i in range(12):
        total += high[i]
    avg = total / 12
    return avg


def averageLow(low):
    total = 0
    for i in range(12):
        total += low[i]
    avg = total / 12
    return avg


def highTemp(high_list):
    high = 0
    for i in range(12):
        temp = high_list[i]
        if temp > high:
            high = temp
    return high


def lowTemp(low_list):
    low = 1000
    for i in range(12):
        temp = low_list[i]
        if temp < low:
            low = temp
    return low


def getData():
    temp = [[],[]]
    print("Enter highest temperatures for each month of the year")
    for i in range(12):
        print("Month",i + 1,end='')
        print(":",end='')
        temp[0].append(int(input()))
        
    print("Enter lowest temperatures for each month of the year")
    for i in range(12):
        print("Month",i + 1,end='')
        print(":",end='')
        temp[1].append(int(input()))

    print("List of highest and lowest temperature for each month of the year")
    for i in range(2):
        for j in range(12):
            print(temp[i][j],end=' ')
        print()
        
    print("Average high temperature for the year ",averageHigh(temp[0]))
    print("Average low temperature for the year ",averageLow(temp[1]))
    print("Highest high temperature for the year ",highTemp(temp[0]))
    print("lowest low temperature for the year ",lowTemp(temp[1]))
    
getData()
