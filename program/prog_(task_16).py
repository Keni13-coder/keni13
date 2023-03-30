from functools import reduce
def number(*bus_stops):
    return sum(map(lambda z:reduce(lambda x,y: x-y,z),bus_stops))

print(number([3,0],[9,1],[4,10],[12,2],[6,1],[7,10]))

# улучшил до бессконечности