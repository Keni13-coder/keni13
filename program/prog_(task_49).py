from functools import reduce
def persistence(n):
    count = 0
    while n >= 10:
        n = reduce(lambda x,y: x * y,[int(x) for x in str(n)])
        count +=1
    return count 
print(persistence(25))


'''
from operator import mul
def persistence(n):
    return 0 if n<10 else persistence(reduce(mul,[int(i) for i in str(n)],1))+1

def persistence(n, count=0):
    return count if n<10 else persistence( eval('*'.join(list(str(n)))), count+1 )


def persistence(n):
    return 0 if n < 10 else persistence(eval('*'.join(str(n)))) + 1
'''