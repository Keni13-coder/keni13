from functools import reduce
def open_or_senior(data):
    return list(map(lambda x: reduce(lambda z,y: "Senior" if z >= 55 and y > 7 else 'Open',x) ,data))



print(open_or_senior([(66, 7), (45, 2), (26, 21), (86, 15), (85, 8), (75, 13)]))