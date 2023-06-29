def open_or_senior(data:list[tuple[int,int]])->list[str]:
    AGE_MIN = 55
    HANDICAP = 7
    return ['Senior' if AGE_MIN<=x[0]>x[-1]>HANDICAP else 'Open' for x in data]
d = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
["Open", "Open", "Senior", "Open", "Open", "Senior"]
print(['Senior' if 55<=i>y>7 else 'Open' for (i,y) in d])