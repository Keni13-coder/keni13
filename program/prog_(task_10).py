
def digitize(n: int):
    return [ int(i) for i in reversed(str(n))]
print(digitize(35231))

def digi(n):
    return list(map(int, str(n)[::-1]))
print(digi(35231))

