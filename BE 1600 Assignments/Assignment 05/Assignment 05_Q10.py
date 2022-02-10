import math



def distance(row, col, data_points):
    ''' calculate distance between P# and the rest of the points '''

    x1 = data_points[row - 1][0]
    y1 = data_points[row - 1][1]

    x2 = data_points[col - 1][0]
    y2 = data_points[col - 1][1]

    distance = math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2 )

    return distance



def data():
    '''store data in list and float the numbers'''
    
    L = []
    f = open("data.txt",'r')
    for line in f:
        line = line.split()
        for i in range(2):
            line[i] = float(line[i])
        L.append(line)
    f.close()

    return L

        

def main():
    data_points = data()
    table = [[] * 9 for i in range(9)]

    # label top row
    table[0].append('')
    for i in range(1,9):
        table[0].append( "P" + str(i) )
        
    # label first column
    for i in range(1,9):
        table[i].append( "P" + str(i) )

    # calculate distance for each datapoint and store into list table
    for row in range(1,9):
        for col in range(1,9):
            table[row].append(distance(row, col, data_points))

    # print 1st row
    for col in range(9):
        print('{0:<6}'.format(table[0][col]), end='')
    print()

    # print every row after 1st
    for row in range(1,9):
        
        # print 1st column
        print('{0:<6}'.format(table[row][0]), end='')

        # prints data points
        for col in range(1,9):
            print('{0:<6.2f}'.format(table[row][col]), end='')
        print()

main()
